# Phone book: name to phone number
# Dictionary lookup is key -> value
# Names have (at least) two parts (normally, in the USA): first and last
# Use a tuple (firstname, lastname) as the key
def make_phonebook() -> dict[tuple[str,str], str | dict[str, str]]:
    names: list[tuple[str,str]] = [('Barrera', 'Joseph'), ('Brown', 'Peter'),
                                   ('Devine', 'Tana'), ('Greenlee', "Tanya"),
                                   ('Harbin', 'Emily'), ('Jensen', 'Douglas'),
                                ('Mangum', 'Amanda'), ('Miller', 'Robert'),
                                ('Smith', 'James'), ('Sorrells', 'Jessica'), 
                                ('Stoneburner', 'Lexi'), ('Vick', 'Allison')]
    numbers: list[str | dict[str,str]] = ['864.596.9128', {'phone' : '864.596.9156',
                                                           'email' : 'peter.brown@converse.edu',
                                                           'office': 'Kuhn 223'},
                          '864.596.9682', '864.596.9088',
                          '864.596.9123', '864.596.9597',
                        '864.596.9127', '864.577.9611',
                        '864.577.2056', '864.596.9149', 
                        '864.596.9049', '864.596.9104']
    result: dict[tuple[str, str], str | dict[str,str]] = {}
    for i in range(len(names)):
        result[names[i]] = numbers[i]
    return result

def name_to_tuple(name: str) -> tuple[str, str]:
    parts: list[str] = name.split(',')
    lastname = parts[0].strip()
    firstname = parts[1].strip()
    return lastname, firstname      # Implicitly creates a tuple

def do_lookup(phonebook: dict[tuple[str,str], str | dict[str,str]], 
              name_tuple: tuple[str, str]) -> str | dict[str, str]:
    return phonebook.get(name_tuple, 'no entry')

def main(args: list[str]) -> int:
    phonebook: dict[tuple[str, str], str | dict[str,str]] = make_phonebook()
    print(phonebook)
    while True:
        response: str = input('Please enter the name of a person to look up, last name first: ').strip()
        #print(f'Response: "{response}"')
        if len(response) == 0:
            break
        elif response.count(',') != 1:
            print('Please enter the name as last name, first name')
        else:
            name_tuple: tuple[str, str] = name_to_tuple(response)
            print(f'{name_tuple[1]} {name_tuple[0]}: {do_lookup(phonebook, name_tuple)}')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
