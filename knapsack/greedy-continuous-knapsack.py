from terminaltables import AsciiTable
print("CIĄGŁY PLECAK")
sizes = [int(x) for x in input('s(wagi/rozmiary)> ').split()]
prices = [int(x) for x in input('w(wartosc)> ').split()]
backpack_size = int(input('rozmiar plecaka (b)> '))

items = []
index = 1
for i in range(len(sizes)):
    items.append({
        'id': index,
        'size': sizes[i],
        'price': prices[i],
        'quantity': 1
    })
    index+=1
items.sort(key=lambda i: i['price']/i['size'], reverse=True)

current_weight = 0
backpack = []
for item in items:
    if item['size'] + current_weight <= backpack_size:
        backpack.append(item)
        current_weight += item['size']
    else:
        item['quantity'] = (backpack_size-current_weight)/item['size']
        backpack.append(item)
        break
print('Wagi i ceny proporcjonalnie do ilości')
table = [['ID', 'Weight', 'Price', 'Ratio', 'Quantity']]
for item in backpack:
    table.append([
        item['id'],
        item['size'] * item['quantity'],
        item['price'] * item['quantity'],
        item['price']/item['size'],
        item['quantity']
    ])
print(AsciiTable(table).table)
print('Waga plecaka: ', sum([i['size']*i['quantity'] for i in backpack]))
print('Wartość plecaka (funkcja celu): ', sum([i['price']*i['quantity'] for i in backpack]))
