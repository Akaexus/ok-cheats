vertexes = input('lista krawedzi> ').split()
print('podawaj luki w formacie {wierzchołek_1}  {wierzchołek_2} {wartosc}')
print('jak konczysz podawanie to wpisz huj')
a = {}
for v1 in vertexes:
    a[v1] = {}
    for v2 in vertexes:
        a[v1][v2] = 0 if v1 == v2 else None
while True:
    string = input('luk> ')
    if string == 'huj':
        break
    v1, v2, distance = string.split()
    a[v1][v2] = int(distance)
print(a)
