def read_seeds(fname: str) -> list[tuple[float, int]]:
    seedlist: list[tuple[float, int]] = []
    with open(fname) as f:
        lines = f.readlines() # Can only be called once
        for i in range(len(lines)):
            lines[i] = lines[i].strip() # Remove the ending newline
            parts: list[str] = lines[i].split(',')
            try:
                x, n = float(parts[0]), int(parts[1])
                if x < 0 or x > 1:
                    raise ValueError(f'seed {x} must be between 0 and 1')
                elif n <= 0:
                    raise ValueError(f'Number of iterations <= 0')
            except (ValueError, IndexError) as e:
                print(f'Error on line {i+1}: "{lines[i]}": {e}')
                continue
            seedlist.append((x, n))
    return seedlist

def main(args: list[str]) -> int:
    print("This program illustrates a chaotic function") 

    seedlist: list[tuple[float, int]] = read_seeds('chaos-seeds.csv')
    for item in seedlist:
        x, n = item  # type: ignore

        # Print table header
        print(f"{'i':^3}\t{'x':^8}")
        print('-' * 16)

        for i in range(n): # type: ignore
            x = 3.9 * x * (1 - x) 
            print(f"{i:^3}\t{x:.6f}")
        print('\n')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
