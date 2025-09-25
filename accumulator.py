def sumlist(numbers: list[float]) -> float:
    # Sum a list of numbers, and return the sum, using the accumulator pattern.
    total: float = 0 # Accumulator variable
    for num in numbers: # Loop
        total = total + num # Update the accumulator variable
    return total

def avglist(numbers: list[float]) -> float:
    # Return the average of a list of numbers, using the accumulator pattern
    total: float = 0 # Accumulator variable #1
    length: int = 0 # Accumulator variable #2
    for num in numbers: # Loop
        total = total + num # Update accumulator variable #1
        length = length + 1 # Update accumulator variable #2
    return total / length

def fact(n: int) -> int:
    # Find a factorial using the accumulator pattern
    prod: int = 1 # Accumulator variable
    for i in range(1,n+1): # Loop
        prod = prod * i # Update the accumulator variable
    return prod

def main(args: list[str]) -> int:
    # Accumulator pattern:
    #    1. Accumulator variable
    #    2. Loop
    #    3. Each time through the loop, update the accumulator to contain more of the answer

    # Read a list of numbers.  To save time, enter it in Python format
    numlist: list[float] = eval(input('Please enter a list in Python format: '))
    print(type(numlist), numlist)
    print('The sum of the list is', sumlist(numlist))
    print('The average of the list is', avglist(numlist))    
    # Find a factorial, using the absolute value of the first number in numlist
    n: int = round(abs(numlist[0]))
    print(n, '! = ', fact(n), sep='')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
