s = 'S'
t = 't'

D = [0, 4, -1, 1, 4]
matrix = [
    [0, 4, None, None, None],
    [None, 0, -5, None, 6],
    [2, None, 0, 2, None],
    [None, None, None, 0, 3],
    [None, None, None, None, 0]
]
vectors = ['S', '1', '2', '3', 't']
A = {} # odleglosci w grafie
for i in range(len(vectors)):
    A[vectors[i]] = {}
    for j in range(len(vectors)):
        A[vectors[i]][vectors[j]] = matrix[i][j]

stack = [t]
v = t
while v != s:
    for u in vectors:
        if A[u][v] is not None and D[vectors.index(u)] + A[u][v] == D[vectors.index(v)]:
            stack.append(u)
            v = u
            break
print(stack)
