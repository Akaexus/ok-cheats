from terminaltables import AsciiTable
import copy
print('wszystkie zadania mają długość jeden')
print('jest tu jeden procesor')
d = [int(x) for x in input('d - linie krytyczne zadań (lista liczb)> ').split()]
w = [int(x) for x in input('w - wagi zadań (lista liczb)> ').split()]
tasks = []

for j in range(len(w)):
    tasks.append({
        'id': j+1,
        'weight': w[j],
        'due-date': d[j],
        'late': False
    })

tasks.sort(key=lambda t: t['weight'], reverse=True)
timeline = [0] * len(w)
for task in tasks:
    if timeline[task['due-date'] - 1] == 0: # slot tuż przed due-date jest wolny
        timeline[task['due-date'] - 1] = task
    else:
        for i in range(len(timeline))[::-1]: # dajemy na ostatni wolny slot
            if timeline[i] == 0:
                if i + 1 > task['due-date']:
                    task['late'] = True
                timeline[i] = task
                break
i = 0
print(0)
for time in timeline:
    print(time)
    i+=1
    print(i)
print("Funkcja celu, czyli suma wag spóźnionych procesów = {}".format(sum([int(t['late']) * t['weight'] for t in tasks])))
