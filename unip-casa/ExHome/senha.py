tentativas = 0

senha = int (input('digite a senha de acesso de 6 digitos \n'))

while tentativas != 3:
    
    if senha == 255310: print('senha correta!!!')
    
    break

else : print('senha incoreata, tente novamente')
tentativas += 1

print('voce utrapassou 3 chances renice')