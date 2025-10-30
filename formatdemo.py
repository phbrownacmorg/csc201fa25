from datetime import date

def print_phone(phone: str) -> None:
    area = phone[:3]
    xchg = phone[3:6]
    ext = phone[-4:]
    print(f'{area}-{xchg}-{ext}: Usual North American')
    print(f'{area}.{xchg}.{ext}: Converse')
    print(f'({area}) {xchg}-{ext}: Old-style North American')
    print(f'+1 {area}-{xchg}-{ext}: include country code')

def print_SSN(ssn: str) -> None:
    print(f"{ssn[:3]}-{ssn[3:5]}-{ssn[-4:]}: SSN") # As SSN
    print(f"{ssn[:5]}-{ssn[-4:]}: Zip+4") # As Zip+4
    print(f"{ssn[:5]}: Zip code") # As zip code

def print_date() -> None:
    month_abbrevs: tuple[str, ...] = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    
    today: date = date.today()
    laborday = date(2025, 9, 1)
    print(f'{today.month}/{today.day}/{today.year}: American')
    print(f'{today.month}/{today.day}/{today.year % 100}: American, 2-digit year')
    print(f'{today.day}/{today.month}/{today.year}: British')
    print(f'{today.day}/{today.month}/{today.year % 100}: British, 2-digit year')
    print(f'{today.day}.{today.month}.{today.year}: European')
    print(f'{today.day}.{today.month}.{today.year % 100}: European, 2-digit year')
    print(f'{today.year}-{today.month}-{today.day}: ISO')
    print(f'{laborday.month}/{laborday.day}/{laborday.year}: Labor Day, American')
    print(f'{laborday.month:02}/{laborday.day:02}/{laborday.year}: Labor Day, American, zeroes')
    print(f'{today.month:02}/{today.day:02}/{today.year}: American, zeroes')
    # Calendar formats
    print(f'{today:%m}/{today:%d}/{today:%Y}: American, zeroes, calendar formats')
    print(f'{today:%A}, {today:%B} {today.day}, {today:%Y}: Full American')
    print(f'{today:%A} {today.day} {today:%B} {today:%Y}: Full British')
    print(f'{today:%d}-{today:%b}-{today:%y}: DOS (Microsoft)')
    print(f'{today.day:02}-{month_abbrevs[today.month-1]}-{today.year%100:02}: DOS, no date format')

def main(args: list[str]) -> int:
    print_phone('8648675309')
    print_SSN('123456789')
    print_date()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
