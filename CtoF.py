def main(args: list[str]) -> int:
    # Input
    degC: float = float(input('Please enter a temperature in Celsius: '))

    # Process (stub)
    degF: float = (9/5) * degC + 32

    # Output
    print(degC, '\u00b0 C = ', degF, '\u00b0 F', sep='')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
