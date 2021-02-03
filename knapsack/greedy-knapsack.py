from terminaltables import AsciiTable
sizes = [int(x) for x in input('s(wagi/rozmiary)> ').split()]
prices = [int(x) for x in input('w(wartosc)> ').split()]
backpack_size = int(input('rozmiar plecaka (b)> '))

items = []
index = 1
for i in range(len(sizes)):
    items.append({
        'id': index,
        'size': sizes[i],
        'price': prices[i]
    })
    index+=1
items.sort(key=lambda i: i['price']/i['size'], reverse=True)

current_weight = 0
backpack = []
for item in items:
    if item['size'] + current_weight <= backpack_size:
        backpack.append(item)
        current_weight += item['size']
table = [['ID', 'Weight', 'Price', 'Ratio']]
for item in backpack:
    table.append([
        item['id'],
        item['size'],
        item['price'],
        item['price']/item['size']
    ])
print(AsciiTable(table).table)
print('Waga plecaka: ', sum([i['size'] for i in backpack]))
print('Wartość plecaka (funkcja celu): ', sum([i['price'] for i in backpack]))
