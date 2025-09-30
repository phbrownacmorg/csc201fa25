from datetime import date

def leapyear(year: int) -> bool:
    leap = False # correct 3/4 of the time
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True

    return leap

def verb_tense(year: int) -> str:
    result = ''
    current_year: int = date.today().year
    if year < current_year:
        result = 'past'
    elif year == current_year:
        result = 'present'
    elif year > current_year:
        result = 'future'
    return result

def verb(year: int) -> str:
    result = ''
    leap: bool = leapyear(year)
    tense: str = verb_tense(year) # 'past', 'present', or 'future'
    if tense == 'future' and leap: # Handle future separately (NOT goes in the middle)
        result = 'will be'
    elif tense == 'future': # and not leap
        result = 'will NOT be' # NOT goes in the middle
    else: # present or past, NOT goes at and
        if tense == 'present':
            result = 'is'
        elif tense == 'past':
            result = 'was'

        # Seperate IF to add (or not add) the NOT        
        if not leap:
            result = result + ' NOT'
    return result
    
def main(args: list[str]) -> int:
    year: int = int(input('Please enter a year that is later than 1582: '))
    print(year, end=' ')
    print(verb(year), end=' ')
    print('a leap year.')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
