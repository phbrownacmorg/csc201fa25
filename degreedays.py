def get_data() -> dict[str, dict[str, int]]:
    return {
'2025-10-01':	{'heating': 0, 'cooling': 6},
'2025-10-02':	{'heating': 0, 'cooling': 3},
'2025-10-03':	{'heating': 3, 'cooling': 0},
'2025-10-04':	{'heating': 3, 'cooling': 0},
'2025-10-05':	{'heating': 0, 'cooling': 2},
'2025-10-06':	{'heating': 0, 'cooling': 3},
'2025-10-07':	{'heating': 0, 'cooling': 7},
'2025-10-08':	{'heating': 0, 'cooling': 10},
'2025-10-09':	{'heating': 0, 'cooling': 5},
'2025-10-10':	{'heating': 5, 'cooling': 0},
'2025-10-11':	{'heating': 4, 'cooling': 0},
'2025-10-12':	{'heating': 0, 'cooling': 3},
'2025-10-13':	{'heating': 0, 'cooling': 6},
'2025-10-14':	{'heating': 0, 'cooling': 1},
'2025-10-15':	{'heating': 0, 'cooling': 1},
'2025-10-16':	{'heating': 0, 'cooling': 0},
'2025-10-17':	{'heating': 3, 'cooling': 0},
'2025-10-18':	{'heating': 0, 'cooling': 2},
'2025-10-19':	{'heating': 0, 'cooling': 2},
'2025-10-20':	{'heating': 8, 'cooling': 0},
'2025-10-21':	{'heating': 7, 'cooling': 0},
'2025-10-22':	{'heating': 6, 'cooling': 0},
'2025-10-23':	{'heating': 10, 'cooling': 0},
'2025-10-24':	{'heating': 11, 'cooling': 0}
    }

def main(args: list[str]) -> int:
    data: dict[str, dict[str, int]] = get_data()
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
