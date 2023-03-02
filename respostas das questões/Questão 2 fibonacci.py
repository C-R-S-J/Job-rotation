n1 = int(input('Digite um número: '))
t1 = n1 - 1
t2 = n1 - 2
if t1 + t2 == n1:
    print(f'O número {n1} faz parte da sequência de fibonacci.')
else :
    print(f'O número {n1} não faz parte da sequência de fibonacci.')