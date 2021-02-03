from terminaltables import AsciiTable

print('earliest due date czy jakos tak')
print('jest tu jeden procesor')
p = [int(x) for x in input('czasy wykonania (lista liczb)> ').split()]
d = [int(x) for x in input('linie krytyczne (lista liczb)> ').split()]
tasks = []
for j in range(len(p)):
    tasks.append({
        'length': p[j],
        'due-date': d[j]
    })
tasks.sort(key=lambda t: t['due-date'])
table = [['Kolejność', "długość", "Linia krytyczna", "Spóźnienie"]]
i = 1
time = 0
for task in tasks:
    time += task['length']
    task['lateness'] = time - task['due-date']
    table.append(
    [str(x) for x in [i, task['length'], task['due-date'], task['lateness']]]
    )
    i+=1
print(AsciiTable(table).table)
print("Funkcja celu czyli maksymalne spóźnienie = {}".format(max([x['lateness'] for x in tasks])))
