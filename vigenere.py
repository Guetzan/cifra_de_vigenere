#coisas pra fazer:
# - função de decifrar
# - possibilitar a encriptação de mais caracteres além de A-Z (provavelmente utilizando UNICODE)
# - adicionar opção de usuário entrar com o texto e chave
# - limitar tamanho do texto a ser cifrado/decifrado em 128 caracteres
# - validar se os caracteres passados no texto estão dentro dos permitidios
# - possibilitar o usuário realizar quantas operações desejar
# - implementar um menu que apresenta as opções possíveis para o usuário: cifrar, decifrar ou sair
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

texto_de_origem = 'helloworld'
chave_em_texto = 'kiosptz'
chave_em_decimal = gerar_chave(chave_em_texto)

#print(gerar_chave(chave_em_texto))
print('Texto de origem:', texto_de_origem)
print('Chave utilizada:', chave_em_texto, '-', end="")
print('', *chave_em_decimal, '', sep=" | ")
print('  Texto cifrado:', cifrar_vigenere(texto_de_origem, chave_em_decimal))














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