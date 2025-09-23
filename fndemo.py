
def change_list(k: int, numlist: list[int]) -> None:
    k = 2 * k
    numlist.append(k)

def main(args: list[str]) -> int:
    k = 7
    list_of_nums = [10, 13, 15]
    print('k =', k, 'list =', list_of_nums)
    change_list(k, list_of_nums)
    # The change to the integer stayed in the function.
    #  The change to the list did not.
    print('k =', k, 'list =', list_of_nums)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
