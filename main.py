# Conversor de celsius p/ fahrenheit e vice e versa

from conversor import celsius_para_fahrenheit, fahrenheit_para_celsius

while True:
        # • Apresentação
        
        print('\n\t\t • Conversor • \n\t\t')

        # • Entrada/Processamento/Saída
        
        print('Escolha uma opção:')
        print('1. Converter de Celsius para Fahrenheit')
        print('2. Converter de Fahrenheit para Celsius')
        print('3. Sair \n')

        opcao = input('Digite o número da opção desejada: ')
        if opcao == '1':
            celsius = float(input('Digite a temperatura em Celsius: '))
            fahrenheit = celsius_para_fahrenheit(celsius)
            print(f"{celsius}ºC é igual a {fahrenheit}ºF")
        elif opcao == '2':
            fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
            celsius = fahrenheit_para_celsius(fahrenheit)
            print(f'{fahrenheit}ºF é igual a {celsius}ºC')
        elif opcao == '3':
            break
        else:
            print('Opção inválida. Tente novamente.')
