# Solicita o nome do usuário
nome = input('Digite seu nome: \n')

# Solicita a idade do usuário (convertendo para inteiro)
idade = int(input('Digite sua idade: \n'))

# Solicita o peso do usuário em kg (convertendo para float)
peso = float(input('Digite seu peso: \n'))

# Solicita a altura do usuário em metros (convertendo para float)
altura = float(input('Digite sua altura: \n'))

# Mostra mensagem inicial
print('Cálculo do IMC')

# Calcula o IMC usando a fórmula: peso / (altura * altura)
imc = peso / (altura * altura)

# Mostra o valor do IMC com duas casas decimais
print(f'Seu IMC é: {imc:.2f}')

# Verifica a classificação do IMC com base em faixas
if 28.5 <= imc < 29.5:
    print('Você é um atleta')
elif imc > 29:
    print('Você precisa emagrecer')  
else:
    print('Você precisa engordar')   