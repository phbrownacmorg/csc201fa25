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
        for i in range(10): # type: ignore
            x = 3.9 * x * (1 - x) 
            print(x)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
