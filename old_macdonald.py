def printVerse(animal: str, sound: str):
    print('Old MacDonald had a farm, E-I-E-I-O!')
    print('And on that farm he had a ' + animal +', E-I-E-I-O!')
    print('With a ' + sound + ', ' + sound + ' here ', end='')
    print('and a ' + sound + ', ' + sound + ' there,')
    print('Here a ' + sound + ', there a ' + sound + ', ', end='')
    print('everywhere a ' + sound + ', ' + sound + '!')
    print('Old MacDonald had a farm, E-I-E-I-O!')
    print()

def main(args: list[str]) -> int:
    printVerse('cow', 'moo')
    printVerse('chicken', 'cluck')
    printVerse('horse', 'neigh')
    printVerse('pig', 'oink')
    printVerse('sheep', 'baa')
    printVerse('goat', 'maa')
    printVerse('turkey', 'gobble')
    printVerse('dog', 'woof')
    printVerse('aardvark', 'slurp')


    # print('Old MacDonald had a farm, E-I-E-I-O!')
    # print('And on that farm he had a cow, E-I-E-I-O!')
    # print('With a moo, moo here and a moo, moo there,')
    # print('Here a moo, there a moo, everywhere a moo, moo!')
    # print('Old MacDonald had a farm, E-I-E-I-O!')
    # print()
    
    # print('Old MacDonald had a farm, E-I-E-I-O!')
    # print('And on that farm he had some chickens, E-I-E-I-O!')
    # print('With a cluck, cluck here and a cluck, cluck there,')
    # print('Here a cluck, there a cluck, everywhere a cluck, cluck!')
    # print('Old MacDonald had a farm, E-I-E-I-O!')
    # print()

    # print('Old MacDonald had a farm, E-I-E-I-O!')
    # print('And on that farm he had a horse, E-I-E-I-O!')
    # print('With a neigh, neigh here and a neigh, neigh there,')
    # print('Here a neigh, there a neigh, everywhere a neigh, neigh!')
    # print('Old MacDonald had a farm, E-I-E-I-O!')
    # print()

    # print('Old MacDonald had a farm, E-I-E-I-O!')
    # print('And on that farm he had a pig, E-I-E-I-O!')
    # print('With an oink, oink here and an oink, oink there,')
    # print('Here an oink, there an oink, everywhere an oink, oink!')
    # print('Old MacDonald had a farm, E-I-E-I-O!')
    # print()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
