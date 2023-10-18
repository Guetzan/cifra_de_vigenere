#coisas pra fazer:
# - implementar função de decifrar
# - possibilitar a encriptação de mais caracteres além de A-Z (provavelmente utilizando UNICODE)
# - limitar tamanho do texto a ser cifrado/decifrado em 128 caracteres [já funcionando para a função cifrar]
# - validar se os caracteres passados no texto estão dentro dos permitidos
# - possibilitar o usuário realizar quantas operações desejar [incompleta]
# - ...

def gerar_chave(texto_chave:str):
    chave = []

    if texto_chave.islower():
        texto_chave = texto_chave.upper()

    for caractere in texto_chave:
        chave.append(ord(caractere) - ord('A'))

    return chave

def cifrar_vigenere(text:str, chave:list):
    texto_cifrado = ''

    for index, caractere in enumerate(text):
        if caractere.islower():
            caractere = caractere.upper()

        caractere_com_shift = ord(caractere) + chave[index % len(chave)] 

        if caractere_com_shift > 90:    
            texto_cifrado += chr(caractere_com_shift - 26)
        else:
            texto_cifrado += chr(caractere_com_shift)

    return texto_cifrado

def solicitar_escolha():
    print('\n-----------------------------------------------')
    print('---------------Cifra de Vigenère---------------')
    print(' [1] - Criptografar   [2] - Descriptografar\n')
    print(' [-]---------------   [4] - Sair            ')
    print('-----------------------------------------------')

    escolha = int(input('Digite sua escolha: '))
    return escolha

def validar_string(string, acao):
    if len(string) > 128:
        print(f'A string ultrapassou em ${len(string) - 128} caracteres o limite de 128. Tente novamente.')

        string = input('Texto: ')

        while(len(string) > 128):
            print(f'Forneça um texto de até 128 caracteres para ser ${acao}.')
            string = input('Texto: ')

    return string

escolha = solicitar_escolha()

while(escolha != 4):
    if(escolha == 1):
        print('Forneça um texto de até 128 caracteres para ser cifrado.')
        texto_de_origem = input('Texto: ')

        print('\nForneça uma chave para ser utilizada.')
        chave_em_texto = input('Chave: ')
        chave_em_inteiros = gerar_chave(chave_em_texto)

        texto_cifrado = cifrar_vigenere(texto_de_origem, chave_em_inteiros)

        print(f'\nTexto de origem: {texto_de_origem}')
        print(f'Chave utilizada: {chave_em_texto} - ', end="")
        print(f'', *chave_em_inteiros, '', sep=" | ")
        print('-----------------------------------------------')
        print(f'Texto cifrado: {texto_cifrado}')
        print('-----------------------------------------------')

    escolha = solicitar_escolha()















###############################################
#Códigos que descartei por enquanto:
###############################################
# def calcular_shift(index_caractere, caractere, chave):
#     #if caractere.isupper():
#     shift_caractere = ord(chave[index_caractere % len(chave)]) - ord('A')

#     #if caractere.islower():
#     #    shift_caractere = ord(chave[index_caractere % len(chave)]) - ord('a')

#     return shift_caractere

# def cifrar_vigenere(text, chave):
#     texto_cifrado = ''

#     for index, caractere in enumerate(text):
#         if caractere.islower():
#             caractere = caractere.upper()

#         shift = calcular_shift(index, caractere, chave)
#         caractere_com_shift = ord(caractere) + shift

#         if caractere_com_shift > 90:    
#             texto_cifrado += chr(caractere_com_shift - 26)
#         else:
#             texto_cifrado += chr(caractere_com_shift)

#     return texto_cifrado
#def adicionar_historico(texto_original, texto_chave, numericos_chave, texto_cifrado)
