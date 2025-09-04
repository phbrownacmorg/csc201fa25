import math

def main(args: list[str]) -> int:
    # Input
    print('This program finds the roots of a quadratic system a*x**2 + b*x + c = 0.')
    a: float = float(input('Please enter a value for a: '))
    b: float = float(input('Please enter a value for b: '))
    c: float = float(input('Please enter a value for c: '))
    print('The system is', a,'* x**2 +', b, '* x +', c, '= 0')

    det: float = b**2 - 4 * a * c
    root1: float = -b + math.sqrt(det) / (2*a)
    root2: float = -b - math.sqrt(det) / (2*a)

    # output
    print('The roots are', root1, 'and', root2)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
