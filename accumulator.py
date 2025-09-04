def main(args: list[str]) -> int:
    # Accumulator pattern:
    #    1. Accumulator variable
    #    2. Loop
    #    3. Each time through the loop, update the accumulator to contain more of the answer

    # Read a list of numbers.  To save time, enter it in Python format
    numlist: list[float] = eval(input('Please enter a list in Python format: '))
    print(type(numlist), numlist)

    # Sum the list, using the accumulator pattern
    total: float = 0 # Accumulator variable
    for num in numlist: # Loop
        total = total + num # Update the accumulator variable
    print('The sum of the list is', total)

    # Find the average of a list, using the accumulator pattern
    total = 0 # Accumulator variable #1
    length: int = 0 # Accumulator variable #2
    for num in numlist: # Loop
        total = total + num # Update accumulator variable #1
        length = length + 1 # Update accumulator variable #2
    print('The average of the list is', total/length)
    
    # Find a factorial using the accumulator pattern
    # Use the absolute value of the first number in numlist
    n: int = round(abs(numlist[0]))
    prod: int = 1 # Accumulator variable
    for i in range(1,n+1): # Loop
        prod = prod * i # Update the accumulator variable
    print(n, '! =', prod)


    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
