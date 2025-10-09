# Calculate the futre value of an investment or loan.  (The math is almost
# identical.)  This version calculates a loan.

# Used https://www.foundersfcu.com/loan-rates to get an idea of used-auto loan rates
# Used https://www.spartanburghonda.com/used-vehicles/ to estimate price

from graphics import *
from typing import cast
import math

def read_pos_float(prompt: str) -> float:
    """Reads a positive floating-point number, using PROMPT.  Returns 0 if
    the input can't be read."""
    result: float = 0
    response: str = input(prompt)
    # Get rid of characters that we can't use as part of the number, but that don't
    #    break things to the point where we can't recover
    dumpable_chars = ',-%$'
    for c in dumpable_chars:
        response = response.replace(c, '')

    # Is it a number?
    if response.count('.') <= 1 and response.replace('.', '').isdecimal():
        result = float(response)

    return result

def read_loan() -> tuple[float, float, int]:
    p: float = read_pos_float('Please enter an amount to borrow: $')
    #float(input('Please enter an amount to borrow: $'))
    # Annual rate
    rate: float = read_pos_float('Please enter the interest rate, in percent: ')
    periods: int = 0
    periodsStr: str = input('How many months are in the life of the loan? ')
    if periodsStr.isdecimal():
        periods = int(periodsStr)
    print('Borrowing $', p, 'at', rate, "% for", periods, 'months:')
    # Loan amount, annual interest rate, number of loan periods
    return p, rate, periods

def calc_balances(p: float, rate: float, periods: int, payment: float):
    # Loan amount, interest rate per loan period (periodic rate),
    #    number of loan periods, fixed payment amount
    balances: list[float] = [p]
    for i in range(periods):    # type: ignore
        # Add the interest
        interest: float = p * rate
        # Update the accumulator
        p = p + interest
        # Subtract the payment
        p = p - payment
        # Record the balance
        balances.append(p)
    return balances

def printTable(balances: list[float], payment: float) -> None:
    # Initial output
    print('Month\tInterest\tPayment\t\tBalance')
    print('-' * 70)
    print('Start\t\t\t\t\t$', balances[0], sep='')

    for i in range(1, len(balances)):
        interest = balances[i] + payment - balances[i-1]
        # Print a table row
        print((i+1), '\t', round(interest,2), '\t', payment, '\t', 
              round(balances[i], 2))

def findTickInterval(max_val: float) -> float:
    MAX_TICKS = 20
    round_nums = [1, 2, 5, 10]
    power_of_ten = math.floor(math.log10(max_val)) - 1
    tick_interval = 10 ** power_of_ten
    for num in round_nums:
        tick_interval = num * (10 ** power_of_ten)
        #print(max_val, tick_interval, max_val / tick_interval)
        if math.floor(max_val / tick_interval) < MAX_TICKS:
            break
    #print(power_of_ten, tick_interval)
    return tick_interval

def drawYTicks(max_y: float, x_margin: float, w: GraphWin) -> None:
    tick_interval: float = findTickInterval(max_y)
    for i in range(int(max_y // tick_interval)+1):
        tick_y = i * tick_interval
        tick: Line = Line(Point(-x_margin * .1, tick_y), Point(0, tick_y))
        tick.draw(w)
        tick_label = Text(Point(-x_margin/2, tick_y), '$' + str(tick_y))
        tick_label.draw(w)

def drawAxes(max_x: float, max_y: float, x_margin: float, y_margin: float,
             w: GraphWin) -> None:
    x_axis = Line(Point(0, 0), Point(max_x + x_margin/2, 0)).draw(w)
    cast(Line, x_axis).setArrow('last')
    y_axis = Line(Point(0, 0), Point(0, max_y + y_margin/2)).draw(w)
    cast(Line, y_axis).setArrow('last')

    # Add tick marks
    drawYTicks(max_y, x_margin, w)

def drawBarGraph(balances: list[float]) -> None:
    # Draw a bar graph
    win: GraphWin = GraphWin('Auto loan balance', 800, 600)
    max_x = len(balances)
    max_y = max(balances)
    margin = 0.1
    x_margin = margin * max_x
    y_margin = margin * max_y
    win.setCoords(-x_margin, -y_margin, max_x + x_margin, max_y + y_margin)

    drawAxes(max_x, max_y, x_margin, y_margin, win)

    for i in range(len(balances)):
        bar = Rectangle(Point(i, 0), Point(i+1, balances[i]))
        bar.setFill('green')
        bar.draw(win)

    win.getMouse()  # Wait for a mouse click
    win.close()

def main(args: list[str]) -> int:
    # Input: get the parameters of the loan
    # Accumulator variable
    p, rate, periods = read_loan()
    payment = 566.14
    if periods > 0 and p > 0:
        balances: list[float] = calc_balances(p, (rate/12)/100, periods, payment)
        printTable(balances, payment)
        drawBarGraph(balances)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
