from terminaltables import AsciiTable
import copy

INFINITE = 9999999

class Knapsack:
    n = 0
    b = 0
    items = {}

    def color(s, color='okblue'):
        return '{}{}{}'.format(Knapsack.colors[color], s, Knapsack.colors['endc'])
    colors = {
        'header':'\033[95m',
        'okblue':'\033[94m',
        'okgreen':'\033[92m',
        'warning':'\033[93m',
        'fail':'\033[91m',
        'endc':'\033[0m',
        'bold':'\033[1m',
        'underline':'\033[4m',
    }

def printDynamicMatrix(matrix):
    table = [['i\j'] + list(map(Knapsack.color, list(range(len(matrix[0])))))]
    for i, row in enumerate(matrix):
        table.append([Knapsack.color(i)] + list(map(lambda x: " " if x == 0 or x == 9999999 else x, row)))
        # table.append([Knapsack.color(i)] + row)
    # table.append([Knapsack.color(i)] + row)
    return '\nDynamic programming array\n' + AsciiTable(table).table


sizes = [int(x) for x in input('s(wagi/rozmiary)> ').split()]
prices = [int(x) for x in input('w(wartosc)> ').split()]
backpack_size = int(input('rozmiar plecaka (b)> '))

max_value = sum(prices)

matrix = []

for i in range(len(sizes) + 1):
    matrix.append([])
    for j in range(max_value + 1):
        matrix[i].append(0)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        size = sizes[i-1]
        price = prices[i-1]
        if i == 0 and j == 0:
            matrix[i][j] == 0
        elif j == 0:
            matrix[i][j] == 0
        elif i == 0 and j >= 1:
            matrix[i][j] = INFINITE
        else:
            if price <= j:
                matrix[i][j] = min(matrix[i-1][j-price] + size, matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]
        # print(printDynamicMatrix(matrix))

print(printDynamicMatrix(matrix))

# BACKTRACKING
def getStartPoint(matrix, backpack_size):
    for j in range(0, len(matrix[0]))[::-1]:
        for i in range(len(matrix)):
            if matrix[i][j] <= backpack_size:
                return j, i
j, i = getStartPoint(matrix, backpack_size)

backpack = []

while j * i:
    if matrix[i][j] == matrix[i-1][j]: # element nie zostal wziety
        i-=1
    else:
        backpack.append(i)
        i-=1
        j-=prices[i]
t = [list(map(Knapsack.color, ['ID', 'Waga', 'Cena']))]
all_size = 0
all_price = 0
for id in backpack:
     t.append([id, sizes[id-1], prices[id-1]])
     all_size += sizes[id-1]
     all_price += prices[id-1]

t.append([Knapsack.color('SUMA'), all_size, all_price])
print("PLECAK! ID liczone od 1.")
print(AsciiTable(t).table)
