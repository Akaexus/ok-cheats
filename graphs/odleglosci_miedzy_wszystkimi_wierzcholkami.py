A = {'1': {'1': 0, '2': '3', '3': None, '4': None, '5': None}, '2': {'1': None, '2': 0, '3': '-2', '4': '-3', '5': '-2'}, '3': {'1': '1', '2': None, '3': 0, '4': '2', '5': None}, '4': {'1': None, '2': None, '3': None, '4': 0, '5': None}, '5': {'1': None, '2': None, '3': None, '4': '1', '5': 0}}


from terminaltables import AsciiTable
import copy
vertexes = list(A.keys())
n = len(vertexes)
table = [list(A.keys())]
for v in A:
    for v2 in A[v]:
        if A[v][v2] is not None:
            A[v][v2] = int(A[v][v2])
    table.append([v] + list(A[v].values()))
print("Macierz sąsiedztwa")
print(AsciiTable(table).table)

D = copy.deepcopy(A)
for k in vertexes:
    for i in vertexes:
        for j in vertexes:
            if D[i][k] is None or D[k][j] is None:
                D[i][j] = D[i][j]
            elif D[i][j] is None:
                D[i][j] = D[i][k] + D[k][j]
            else:
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

print('Tablicowanie funkcji')
table = [list(D.keys())]
for v in D:
    table.append([v] + list(D[v].values()))
print(AsciiTable(table).table)
