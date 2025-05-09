nome = input ('Digite seu nome \n')

idade = int (input ('Digite sua idade: \n'))

peso = float (input('Digite seu peso: \n'))

altura = float (input('Digite sua altura: \n'))

print ('Calculo do ImC')

imc = (peso / (altura * altura))

if imc == 29: print ('voce um atleta')

elif imc > 29 : print ('voce precisa esmagrecer')

else : print ('voce precisa engorda')