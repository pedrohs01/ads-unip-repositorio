# Solicita o nome do usuário e armazena em uma variável
nome = input('Digite seu nome: ')

# Solicita a idade do usuário e converte para inteiro
idade = int(input('Digite sua idade: '))

# Solicita o peso do usuário em kg e converte para float
peso = float(input('Digite seu peso (kg): '))

# Solicita a altura do usuário em metros e converte para float
altura = float(input('Digite sua altura (m): '))

# Calcula o IMC utilizando a fórmula: peso dividido pela altura ao quadrado
imc = peso / (altura ** 2)

# Exibe o resultado formatado com duas casas decimais
print(f'\nOlá, {nome}. Seu IMC é {imc:.2f}')

# Verifica em qual faixa de classificação o IMC se encaixa e imprime o resultado apropriado

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está com o peso normal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 35:
    print('Você está com obesidade grau I.')
elif 35 <= imc < 40:
    print('Você está com obesidade grau II.')
else:
    print('Você está com obesidade grau III (mórbida).')
