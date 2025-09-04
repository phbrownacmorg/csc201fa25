# Calculate the futre value of an investment or loan.  (The math is almost
# identical.)  This version calculates a loan.

# Used https://www.foundersfcu.com/loan-rates to get an idea of used-auto loan rates
# Used https://www.spartanburghonda.com/used-vehicles/ to estimate price

def main(args: list[str]) -> int:
    # Input: get the parameters of the loan
    # Accumulator variable
    p: float = float(input('Please enter an amount to borrow: $'))
    rate: float = float(input('Please enter the interest rate, in percent: '))
    periods: int = int(input('How many months are in the life of the loan? '))


    # Initial output
    print('Borrowing $', p, 'at', rate, "% for", periods, 'months:')
    print('Month\tInterest\t\tPayment\t\tBalance')
    print('-' * 70)
    print('Start\t\t\t\t\t\t$30000')

    payment: float = 566.14
    monthly_rate: float = (rate / 12) / 100
    # Process (with output included)
    for i in range(periods): # Loop for the accumulator pattern
        # Add the interest
        interest: float = p * monthly_rate
        # Update the accumulator
        p = p + interest

        # Subtract the payment
        p = p - payment

        # Print the new balance
        print((i+1), '\t', interest, '\t', payment, '\t', p)



    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
