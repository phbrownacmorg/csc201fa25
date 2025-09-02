def main(args: list[str]) -> int:
    # Input
    degC: float = float(input('Please enter a temperature in Celsius: '))

    # Process (stub)
    degF: float = (9/5) * degC + 32

    # Output
    print(degC, 'degrees Celsius is', degF, 'degrees Fahrenheit')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
