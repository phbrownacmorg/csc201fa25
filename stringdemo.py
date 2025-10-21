def int2str(digits: str) -> int:
    sign = 1
    # Check for minus
    if digits[0] == '-':
        sign = -1
        digits = digits[1:]
    # At this point, we should have *only* digits
    if not digits.isdigit():
        raise ValueError('integer cannot have non-digits')
    # Now, find the absolute value.
    value = 0
    for d in digits:
        value = 10 * value + (ord(d) - ord('0'))
    return sign * value

def main(args: list[str]) -> int:
    s: str = 'apple'

    i = 0
    for ch in s:
        print(i, s[i], ch, s[(-2*i+5) % -len(s)], (-2*i+5) % -len(s), s[-i-1], -i-1)    
        i = i+1

    for i in range(len(s)):
        print(i, s[:i], s[i:], s[:-i-1], s[-i-1:], s[:i:2], s[i::2], s[::i+1], s[::-i-1])

    intstr: str = input('Please enter an integer: ')
    num = int2str(intstr)
    print("'" + intstr + "'", "'" + (intstr*2) + "'", num, num*2)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
