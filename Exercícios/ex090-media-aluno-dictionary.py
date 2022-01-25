# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a
# situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

student = dict()

student['name'] = str(input('Name: '))
student['average'] = float(input(f'Type {student["name"]} s Average: '))

if student['average'] >= 7:
    student['situation'] = 'Approved'
elif 5 <= student['average'] < 7:
    student['situation'] = 'Recovery'
else:
    student['situation'] = 'disapproved'
print('-=' * 20)
for k, v in student.items():
    print(f' - {k} is igual to: {v}')
