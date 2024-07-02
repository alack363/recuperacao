# Calculadora de média
# Desenvolvido por
# Kaidy Alack do 2B
# Ana Clara de Lima 2B

from calc_media import CalculadoraMedia

nota1 = float(input('digite a nota 1: '))

while nota1 < 0 or nota1 > 10:
    print('A nota não pode ser menor que 0 ou maior que 10')
    nota1 = float(input('digite novamente'))

nota2 = float(input('digite a nota 2: '))

while nota2 < 0 or nota2 > 10:
    print('A nota não pode ser menor que 0 ou maior que 10')
    nota2 = float(input('digite novamente'))

nota3 = float(input('digite a nota 3: '))

while nota3 < 0 or nota3 > 10:
    print('A nota não pode ser menor que 0 ou maior que 10')
    nota3 = float(input('digite novamente'))

resultado = CalculadoraMedia.calcular(nota1, nota2, nota3)
print('resultado', resultado)