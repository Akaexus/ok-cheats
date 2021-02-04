s = '1'
vectors = ['1', '2','3', '4', '5']
matrix = [
    [0, 4, None, None, None],
    [None, 0, 5, 3, None],
    [-1, None, 0, -2, -3],
    [None, None, None, 0, 1],
    [None, None, None, None, 0]
]
D = {}
for v in vectors:
    D[v] = None
A = {} # odleglosci w grafie
for i in range(len(vectors)):
    A[vectors[i]] = {}
    for j in range(len(vectors)):
        A[vectors[i]][vectors[j]] = matrix[i][j]

for v in vectors:
    D[v] = A[s][v]
    D[s] = 0
for k in range(len(vectors) - 2):
    for v in vectors:
        if v != s:
            for u in vectors:
                if D[u] is None or A[u][v] is None:
                    D[v] = D[v]
                elif D[v] is None:
                    D[v] = D[u] + A[u][v]
                else:
                    D[v] = D[v]
print(D)
