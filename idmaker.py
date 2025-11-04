from csv import DictReader, DictWriter

def read_names(filename: str) -> list[dict[str,str]]:
    namelist: list[dict[str,str]] = []
    with open(filename) as f:
        reader = DictReader(f)
        for row in reader:
            for key in row.keys():
                row[key] = row[key].strip() # Remove white space from the ends of the names
            namelist.append(row)
    return namelist

def make_id(namedict: dict[str,str]) -> str:
    id = namedict['lastname']
    oddchars = " '"
    for c in oddchars:
        id = id.replace(c, '')

    othernames = namedict['firstname'].split() # Split given names on spaces
    initials = ''
    for name in othernames:
        initials = initials + name[0]
    id = initials[:2].upper() + id

    return id + '001'

def write_ids(namelist: list[dict[str, str]], filename: str) -> None:
    # newline='' below is needed to prevent blank lines
    #   between the rows
    with open(filename, 'w', newline='') as f:
        #['lastname', 'firstname', 'userid']
        fields = namelist[0].keys() 
        writer = DictWriter(f, fields)

        writer.writeheader()
        for entry in namelist:
            writer.writerow(entry)
    


def main(args: list[str]) -> int:
    # names = ['Brown, Peter H.',
    #          'Feitzinger, Laura',
    #          'von Richthofen, Manfred Albrecht ',
    #          'Windsor, William Arthur Philip Louis',
    #          'Brinch Hansen, Per',
    #          "De Villier, Daphne",
    #          'Sanchez Cazares, Vanessa Itzel',
    #          'Grant-Ponce, Jamie',
    #          "O'Brian, Brian B."
    #          ]

    names: list[dict[str,str]] = read_names('names.csv')
    for name in names:
        name['userid'] = make_id(name)
        #print(f"{name['lastname']}, {name['firstname']}: {name['userid']}")
    write_ids(names, 'userids.csv')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
