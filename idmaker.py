def make_id(name: str) -> str:
    id = name

    parts = name.split(',')
    id = parts[0]           # Last name
    oddchars = " '"
    for c in oddchars:
        id = id.replace(c, '')

    othernames = parts[1].split() # Split given names on spaces
    initials = ''
    for name in othernames:
        initials = initials + name[0]
    id = initials[:2].upper() + id

    return id + '001'

def main(args: list[str]) -> int:
    names = ['Brown, Peter H.',
             'Feitzinger, Laura',
             'von Richthofen, Manfred Albrecht ',
             'Windsor, William Arthur Philip Louis',
             'Brinch Hansen, Per',
             "De Villier, Daphne",
             'Sanchez Cazares, Vanessa Itzel',
             'Grant-Ponce, Jamie',
             "O'Brian, Brian B."
             ]
    
    for name in names:
        print(name + ":", make_id(name))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
