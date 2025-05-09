# Inicializa a variável de tentativas com 0
tentativas = 0

# Define a senha correta (você pode esconder isso depois, claro)
senha_correta = 255310

# Laço enquanto o número de tentativas for menor que 3
while tentativas < 3:
    
    # Solicita a senha do usuário
    senha = int(input('Digite a senha de acesso de 6 dígitos: '))
    
    # Verifica se a senha está correta
    if senha == senha_correta:
        print('Senha correta!!!')
        break  # Sai do laço se acertar
    else:
        print('Senha incorreta, tente novamente.')

    # Incrementa o número de tentativas
    tentativas += 1

# Se o usuário errou 3 vezes, mostra a mensagem final
if tentativas == 3:
    print('Você ultrapassou 3 tentativas. Reinicie o processo.')
