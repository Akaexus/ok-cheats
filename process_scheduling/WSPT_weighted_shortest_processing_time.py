from terminaltables import AsciiTable

print('czyli według malejcego ratio wi / pj (waga do czasu trwania)\nmiara jakości to Suma ilorazów wag zadań * czas zakończenia')
print('jest tu jeden procesor')
p = [int(x) for x in input('czasy wykonania (lista liczb)> ').split()]
w = [int(x) for x in input('wagi zadań (lista liczb)> ').split()]
tasks = []
for j in range(len(p)):
    tasks.append({
        'length': p[j],
        'weight': w[j],
        'ratio_factor': w[j]/p[j]
    })

tasks.sort(key=lambda t: t['ratio_factor'], reverse=True)
i = 1
table = [["LP", "Długość", "Waga", "wi/pi", 'Czas zakończenia']]
time = 0
for task in tasks:
    time += task['length']
    task['complete_time'] = time
    table.append([
        i,
        task['length'],
        task['weight'],
        task['ratio_factor'],
        task['complete_time']
    ])
    i+=1
print(AsciiTable(table).table)
print('wj - waga\ncj - czas zakończenia zadania')
print('Funkcja celu, suma wj*cj: ', sum([t['weight'] * t['complete_time'] for t in tasks]))
