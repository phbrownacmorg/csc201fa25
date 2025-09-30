import math


def readSystem() -> tuple[float, float, float]:
    # Input
    print('This program finds the roots of a quadratic system a*x**2 + b*x + c = 0.')
    a: float = float(input('Please enter a value for a: '))
    b: float = float(input('Please enter a value for b: '))
    c: float = float(input('Please enter a value for c: '))
    print('The system is', a,'* x**2 +', b, '* x +', c, '= 0')
    return a, b, c

def main(args: list[str]) -> int:
    a, b, c = readSystem()
    det: float = b**2 - 4 * a * c
    # 3-way decision
    if det < 0:
        print('The system has no real roots.')
    elif det == 0:
        root: float = -b / (2*a)
        # 1-way decision
        if root == -0.0:
            root = 0    # Shouldn't print -0
        print('The system has two coincident roots at', root)
    else:
        root1: float = (-b + math.sqrt(det)) / (2*a)
        root2: float = (-b - math.sqrt(det)) / (2*a)

        # output
        print('The roots are', root1, 'and', root2)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
