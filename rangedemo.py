def main(args: list[str]) -> int:
    # Regular range: range(n) gives [0,1,...n-1]
    print('range(4) =', list(range(4)))
    # Negative n gets wonky (empty result)
    print('range(-7) =', list(range(-7)))

    # Two-argument range(): range(start, end) gives [start, start+1, ..., end-1]
    print('range(3, 10) =', list(range(3, 10)))
    print('range(-12, -3) =', list(range(-12, -3)))

    # Three-argument version: range(start, stop, step) gives [start, start+step, ..., ] up to end
    print('range(5, 22, 5) =', list(range(5,22,5)))
    # Counting down
    print('range(7, -1, -1) =', list(range(7, -1, -1)))
    # Counting multiples of 3.  Note end value is not included.
    print('range(0, 15, 3) =', list(range(0, 15, 3)))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
