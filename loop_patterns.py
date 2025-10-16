def definite_loop(iterations: int) -> list[int]:
    result: list[int] = []
    for i in range(iterations):
        result.append(i**2)
    return result

def definite_with_while(iterations: int) -> list[int]:
    result: list[int] = []
    i = 0
    while i < iterations:
        result.append(i**2)
        i = i+1   # Very important!
    return result

def interactive_loop() -> tuple[list[float], float, float]:
    numlist: list[float] = []
    sum = 0
    length = 0

    response = 'Y'
    while response == 'Y':
        num = float(input('Please enter a number: '))
        numlist.append(num)
        sum = sum + num
        length = length + 1
        response = input('Do you want to enter another number? (Y/N) ')  # This gets tedious
    return numlist, sum, sum/length


def interactive_sentinel_loop() -> tuple[list[float], float, float]:
    numlist: list[float] = []
    total = 0
    length = 0

    # Interactive loop, using a non-number as the sentinel
    while True: # Yes, this is an infinite loop if I don't break out
        response = input('Please enter a number, or hit Enter to exit: ')
        try:
            num = float(response) # Exception if the user entered a non-number
        except ValueError:
            break
        else:
            numlist.append(num)
            total = total + num
            length = length + 1

    return numlist, total, total/length

def main(args: list[str]) -> int:
    print(definite_loop(5))
    print(definite_with_while(5))
    numlist, total, average = interactive_sentinel_loop()
    print('The sum of the list ', numlist, ' is ', total, '. The average is ',
           average, '.', sep='')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
