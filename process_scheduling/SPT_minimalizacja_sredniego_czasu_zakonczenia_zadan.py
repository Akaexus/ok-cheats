from terminaltables import AsciiTable

print('funkcją kosztu jest suma czasów zakończenia zadań, co jest równoważne minimalizacji średniego czasu przepływu')
print('jest tu jeden procesor')
p = [int(x) for x in input('czasy wykonania (lista liczb)> ').split()]
print(sorted(p))
