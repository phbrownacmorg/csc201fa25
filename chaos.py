def main(args: list[str]) -> int:
    print("This program illustrates a chaotic function") 
    try:
        x = float(input("Enter a number between 0 and 1: ")) 
        if not 0 < x < 1:
            # If I raise my own exception, I can choose the message
            raise ValueError(str(x) + ' is not between 0 and 1.')
    except ValueError as e:
        if 'could not convert' in e.args[0] :
            print('That input was not a number.')
        else:
            print(e.args[0])
    else:
        # Print table header
        print(f"{'i':^3}\t{'x':^8}")
        print('-' * 16)

        for i in range(150): # type: ignore
            x = 3.9 * x * (1 - x) 
            print(f"{i:^3}\t{x:.6f}")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
