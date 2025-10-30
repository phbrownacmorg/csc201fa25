def print_weekday_names() -> None:
    weekday_names: tuple[str, ...] = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
                                'Thursday', 'Friday', 'Saturday')
    
    # Create three-letter abbrevs using the accumulator pattern
    weekday_3LA: list[str] = []
    for name in weekday_names:
        weekday_3LA.append(name[:3])
    # Create three-letter abbreviations using a list comprehension
    weekday_3LA_2: tuple[str, ...] = tuple([d[:3] for d in weekday_names])
    print(f'{weekday_names}\n{weekday_3LA}\n{weekday_3LA_2}')

def string_to_number_list(s: str) -> list[float]:
    result: list[float] = []
    tokens = s.strip().split()
    for token in tokens: #Iteration over a list by value
        try:
            result.append(float(token)) # Append an object to a list
        except ValueError:
            pass # Ignore any token that doesn't convert
    return result

def read_numbers() -> list[float]:
    numlist: list[float] = []
    while True:
        inString: str = input('Please enter one or more numbers, separated by spaces, or Enter to stop: ')
        newNums = string_to_number_list(inString)
        if len(newNums) == 0:
            break
        numlist.extend(newNums) # Extend a list with another list
    return numlist

def sumlist(numbers: list[float]) -> float:
    # Accumulator pattern
    total: float = 0
    for i in range(len(numbers)): # Iterate over a list by index (could have been done by value)
        total = total + numbers[i]
    return total

def sort(numbers: list[float]) -> None:
    for i in range(len(numbers)):
        value: float = numbers.pop() # Grab the last number
        j = 0
        while j < i: # Build up a sorted sublist from the beginning of the list
            if j < len(numbers) and value < numbers[j]:
                break
            j = j+1
        numbers.insert(j, value)

def main(args: list[str]) -> int:
    print_weekday_names()

    # Read a bunch of numbers
    numlist: list[float] = read_numbers()
    print(numlist)

    # Find the sum
    print(f'The sum of the numbers is {sumlist(numlist)} = {sum(numlist)}')

    # Sort the numbers
    sort(numlist)
    print(numlist)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
