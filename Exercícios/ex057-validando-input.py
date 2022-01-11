# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input(
    'Digite o Sexo [(F)eminino / (M)asculino / (N)ão-Binário / N(A)N]: ')).strip().upper()
while sexo not in 'FMNA':
    sexo = str(
        input('Dados inválidaos. Por favor, use apenas F ou M: ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))

