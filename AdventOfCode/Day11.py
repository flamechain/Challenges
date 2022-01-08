
flashes = 0

class Item:
    def __init__(self, number):
        self.number = number
        self.beenFlashed = False

def incrementArray(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j].number += 1
            array[i][j].beenFlashed = False

def checkFlash(array, x, y):
    global flashes

    if array[x][y].number > 9 and array[x][y].beenFlashed == False:
        array[x][y].beenFlashed = True
        flashes += 1
        incrementSurroundings(array, x, y)

def incrementSurroundings(array, x, y):
    for i in range(x-1, x+1+1):
        for j in range(y-1, y+1+1):
            try:
                array[i][j].number += 1
            except IndexError:
                pass

    for i in range(x-1, x+1+1):
        for j in range(y-1, y+1+1):
            try:
                checkFlash(array, i, j)
            except IndexError:
                pass

def main():
    global flashes

    with open("Day11.txt", 'r') as f:
        array = []
        line = []

        for i in f.readlines():
            i = i.strip()
            line = [Item(int(j)) for j in i]
            array.append(line)

    for i in range(10):
        incrementArray(array)

        for x  in range(len(array)):
            for y in range(len(array[x])):
                checkFlash(array, x, y)

        for x  in range(len(array)):
            for y in range(len(array[x])):
                if array[x][y].number > 9:
                    array[x][y].number = 0

        for x in array:
            for y in x:
                print(y.number, end='')
            print()
        print()
        print(flashes)
        print()

    return flashes

print(main())
