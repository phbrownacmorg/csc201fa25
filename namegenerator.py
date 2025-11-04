import random
from bisect import bisect
from csv import DictReader
from typing import cast

def read_namedict(filename: str, cum_freq_key: str) -> list[dict[str, str | float]]:
    result: list[dict[str, str | float]] = []
    with open(filename, 'r') as csvfile:
        reader = DictReader(csvfile)
        for row in reader:
            result.append(row)
    total_freq = float(result.pop()[cum_freq_key])
    for record in result:
        record['freq'] = float(record[cum_freq_key]) / total_freq
    return result

def getfreq(item: dict[str, str | float]) -> float:
    return cast(float, item['freq'])

def get_name(namelist: list[dict[str, str | float]], namekey: str) -> str:
    x: float = random.random() # 0 <= x < 1
    j: int = bisect(namelist, x, key=getfreq)
    return cast(str, namelist[j-1][namekey]).capitalize()

def main(args: list[str]) -> int:
    # How many names are we going to generate?
    n: int = int(input('How many names should be generated? '))

    # Read the names
    first_names: list[dict[str,str|float]] = read_namedict('first-names.csv', 'Cum%')
    last_names:  list[dict[str,str|float]] = read_namedict('last-names.csv', 'cum_prop100k')
    
    # Generate the names and store them in a list
    namelist: list[str] = []
    for i in range(n):
        # Last name
        thisname = get_name(last_names, 'name') + ","
        # First name
        thisname = thisname + get_name(first_names, 'Name')

        # Middle name(s).  Assume they're all the same kind (first names or last names).
        # How many?
        breakpoints: list[float] = [0.2, 0.97, 0.99]
        x = random.random()
        num_names: int = bisect(breakpoints, x)

        if num_names > 0:
            # What kind?  Default to first names.
            dictlist = first_names
            namekey = 'Name'
            x = random.random()
            if x < 0.3:
                dictlist = last_names
                namekey = 'name'
            for i in range(num_names):
                thisname = thisname + ' ' + get_name(dictlist, namekey)

        namelist.append(thisname)
    #print(namelist)

    # Write the names to an output file
    with open('names.csv', 'w') as outfile:
        # Write column headers
        outfile.write('lastname,firstname\n')
        for name in namelist:
            outfile.write(name + '\n')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))