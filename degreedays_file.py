def get_data(filename: str) -> dict[str, dict[str, int]]:
    result: dict[str, dict[str, int]] = {}
    with open(filename) as f:
        for line in f.readlines()[1:]: # Ignore the first line
            parts: list[str] = line.split(',')
            result[parts[0]] = {'heating': int(parts[1]),
                                'cooling': int(parts[2])}
    return result

def main(args: list[str]) -> int:
    data: dict[str, dict[str, int]] = get_data('degreedays.csv')
    # Accumulator variables, initially 0
    sums: dict[str, int] = {}

    # Accumulator loop
    for date, day_values in data.items(): # type: ignore
        # Update the accumulator variables
        for day_key in day_values.keys():
            # Creates missing categories automatically
            sums[day_key] = sums.get(day_key, 0) + day_values[day_key]

    print(sums)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
