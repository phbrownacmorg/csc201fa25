def parseInput(age_str: str, cit_str: str) -> tuple[int, int]:
    """Takes two strings, one representng a person's age and the other
        representing how long the person has been a U.S. citizen.
        Parses both as integers, verifies that they are non-negative,
        and returns them."""
    age = -1
    citizenship = -1
    try:
        age = int(age_str)
    except ValueError:
        raise ValueError('Age must be a non-negative integer.')
    try:
        citizenship = int(cit_str)
    except ValueError:
        raise ValueError('Years of citizenship must be a non-negative integer.')
    
    if age < 0:
        raise ValueError('Age cannot be negative.')
    if citizenship < 0:
        raise ValueError('Years of citizenship cannot be negative.')
    if age < citizenship:
        raise ValueError('Years of citizenship cannot be greater than age.')

    return age, citizenship

def readInput() -> tuple[int, int]:
    """Reads two integers, one for age and one for the years of citizenship,
        from the keyboard, and returns them."""
    age_str = input("Please enter a person's age: ")
    cit_str = input('How many years has this person been a U.S. citizen? ')
    return parseInput(age_str, cit_str)

def eligibleHR(age: int, cit: int) -> bool:
    """Takes two positive integers AGE and CIT (how long the person has been a
        U.S. citizen), and returns a boolean indicating whether the person
        is eligible to servve in the U.S. House of Representatives."""
    return False

def eligibleSenate(age: int, cit: int) -> bool:
    """Takes two positive integers AGE and CIT (how long the person has been a
        U.S. citizen), and returns a boolean indicating whether the person
        is eligible to servve in the U.S. Senate."""
    return False

def main(args: list[str]) -> int:
    age, citizen = readInput()
    print(f'A person of age {age}, who has been a U.S. citizen for {citizen} years is ',
          end='')
    if not eligibleHR(age, citizen):
        print('NOT ', end='')
    print('eligible to serve in the U.S. House of Representatives.')
    print('The same person is ',end='')
    if not eligibleSenate(age, citizen):
        print('NOT ', end='')
    print('eligible to serve in the U.S. Senate.')


    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
