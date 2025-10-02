# Read a Social Security number, and print out whether it has the
# right form to be a valid Social Security number. Criteria from
# https://primepay.com/learn/payroll/how-to-determine-a-valid-social-security-number/

def valid_ssn_form(ssn: str) -> bool:
    valid_form: bool = True
    # Is it the right length?
    if len(ssn) != 9 and len(ssn) != 11:
        valid_form = False
    # If it has hyphens, are they in the right places?
    elif len(ssn) == 11 and (ssn[3] != '-' or ssn[6] != '-'):
        valid_form = False
    # Does it have exactly 9 digits?
    ssn = ssn.replace('-', '') # Get rid of the hyphens
    if not (len(ssn) == 9 and ssn.isdigit()):
        valid_form = False
    # First group
    elif (ssn[0:3] == '000' or ssn[0:3] == '666' or ssn[0:3] > '773'):
        valid_form = False
    # Second group
    elif (ssn[3:5] == '00'):
        valid_form = False
    # Third group
    elif (ssn[5:] == '0000'):
        valid_form = False
    # Not in sequence
    elif ssn == '123456789':
        valid_form = False

    return valid_form

def main(args: list[str]) -> int:
    # Read the SSN
    ssn: str = input('Please enter a Social Security number: ')
    print('"' + ssn + '" is', end=' ')
    if not valid_ssn_form(ssn):
        print('NOT', end=' ')
    print('in the right form to be a valid Social Security number.')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
