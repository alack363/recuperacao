from calc_temp import Temperatura


print('''
1 #[1]. transformar celsius para fahrenheit
2 #[2]. transformar fahrenheit para celsius
''') 

main = float(input('escolha uma opção acima: '))

if main == 1:
    celsius = float(input('Digite a temperatura em graus Celsius: '))
    resultado = Temperatura.celsius_para_fahren(celsius)
    print(f'{celsius} graus Celsius equivalem a {resultado:.2f} graus Fahrenheit.')
    pass

elif main == 2:
    fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))
    resultado = Temperatura.fahrenheit_para_celsius(fahrenheit)
    print(f'{fahrenheit} graus Fahrenheit equivalem a {resultado:.2f} graus Celsius.')
    pass

else:
        print('Essa opção não existe, por favor escolha entre 1 ou 2')
