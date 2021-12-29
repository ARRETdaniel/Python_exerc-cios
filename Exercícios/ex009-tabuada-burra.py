print('\nTabuada\n')
x = 10 # = int(input('Digite um número para exibir sua tabuada: '))

print('{:-^15}'.format(x))

for num in range(10):
    print('{} x {:2} = {}'.format(x, num, (x*num)))
#print('{} x {:2} = {}'.format(x, 2, (x*2)))
#print('{} x {:2} = {}'.format(x, 3, (x*3)))
#print('{} x {:2} = {}'.format(x, 4, (x*4)))
#print('{} x {:2} = {}'.format(x, 5, (x*5)))
#print('{} x {:2} = {}'.format(x, 6, (x*6)))
#print('{} x {:2} = {}'.format(x, 7, (x*7)))
#print('{} x {:2} = {}'.format(x, 8, (x*8)))
#print('{} x {:2} = {}'.format(x, 9, (x*9)))
#print('{} x {:2} = {}'.format(x, 10, (x*10)))
print('-' * 15)
