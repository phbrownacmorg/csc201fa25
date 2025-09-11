# Calculate the futre value of an investment or loan.  (The math is almost
# identical.)  This version calculates a loan.

# Used https://www.foundersfcu.com/loan-rates to get an idea of used-auto loan rates
# Used https://www.spartanburghonda.com/used-vehicles/ to estimate price

from graphics import *
import math

def main(args: list[str]) -> int:
    # Input: get the parameters of the loan
    # Accumulator variable
    p: float = float(input('Please enter an amount to borrow: $'))
    rate: float = float(input('Please enter the interest rate, in percent: '))
    periods: int = int(input('How many months are in the life of the loan? '))

    balances: list[float] = [p]
    # Initial output
    print('Borrowing $', p, 'at', rate, "% for", periods, 'months:')
    print('Month\tInterest\tPayment\t\tBalance')
    print('-' * 70)
    print('Start\t\t\t\t\t$', p, sep='')

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
        print((i+1), '\t', round(interest,2), '\t', payment, '\t', round(p, 2))
        balances.append(p)
    


    #print(balances)

    # Draw a bar graph
    win: GraphWin = GraphWin('Auto loan balance', 800, 600)
    max_x = periods
    max_y = max(balances)
    margin = 0.1
    x_margin = margin * max_x
    y_margin = margin * max_y
    win.setCoords(-x_margin, -y_margin, max_x + x_margin, max_y + y_margin)

    # Draw axes
    x_axis = Line(Point(0, 0), Point(max_x + x_margin/2, 0))
    x_axis.setArrow('last')
    x_axis.draw(win)
    y_axis = Line(Point(0, 0), Point(0, max_y + y_margin/2))
    y_axis.setArrow('last')
    y_axis.draw(win)

    # Add labels and tick marks
    #MIN_TICKS = 5
    MAX_TICKS = 20
    round_nums = [1, 2, 5, 10]
    power_of_ten = math.floor(math.log10(max_y)) - 1
    tick_interval = 10 ** power_of_ten
    for num in round_nums:
        tick_interval = num * (10 ** power_of_ten)
        print(max_y, tick_interval, max_y / tick_interval)
        if math.floor(max_y / tick_interval) < MAX_TICKS:
            break
    print(power_of_ten, tick_interval)

    # draw Y ticks
    for i in range(int(max_y // tick_interval)+1):
        tick_y = i * tick_interval
        tick: Line = Line(Point(-x_margin * .1, tick_y), Point(0, tick_y))
        tick.draw(win)
        tick_label = Text(Point(-x_margin/2, tick_y), '$' + str(tick_y))
        tick_label.draw(win)

    for i in range(len(balances)):
        bar = Rectangle(Point(i, 0), Point(i+1, balances[i]))
        bar.setFill('green')
        bar.draw(win)

    win.getMouse()  # Wait for a mouse click
    win.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
