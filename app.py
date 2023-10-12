from gtts import gTTS
import os

# Função para transformar texto em áudio e salvar ou reproduzir
def texto_audio(texto, nome_do_arquivo, salvar=True):
    tts = gTTS(text=texto, lang='pt-br')  # Use 'pt-br' para português do Brasil
    tts.save(nome_do_arquivo)
    
    if salvar:
        print(f'Áudio salvo como "{nome_do_arquivo}"')
    else:
        os.system(f"start {nome_do_arquivo}")

while True:
    try:
        texto = input('Digite o texto que deseja transformar em áudio: ')
        nome_do_arquivo = input('Digite o nome do arquivo que deseja criar: ')
        nome_do_arquivo += '.mp3'

        print('Deseja salvar ou apenas reproduzir? ')
        print('1: Salvar')
        print('2: Reproduzir')
        opcao = input('Digite 1 para salvar ou 2 para reproduzir: ')
        opcao = int(opcao)  # Converte para inteiro

        if opcao == 1:
            texto_audio(texto, nome_do_arquivo, salvar=True)
        elif opcao == 2:
            texto_audio(texto, nome_do_arquivo, salvar=False)

        continuar = input('Deseja continuar? (Digite "sair" para encerrar): ')
        if continuar.lower() == 'sair':
            break
    except ValueError: 
        print('Digite um valor inteiro para a opção (1 ou 2).')





































# from gtts import gTTS
# import os

# # Texto que você deseja transformar em áudio
# def texto_audio(texto,nome_do_arquivo  ):
#     # Crie um objeto gTTS
#     tts = gTTS(text=texto, lang='pt-br')  # Use 'pt-br' para português do Brasil
#   # Salve o áudio em um arquivo MP3
#     tts.save(nome_do_arquivo)
#     # Reproduza o áudio
#     os.system(f"start {nome_do_arquivo}")


# while True:
#     try:
#         texto = input('Digite o texto que deseja tranformar em audio:  ')
#         nome_do_arquivo = input('Digite o nome do arquivo que deseja criar ')
#         nome_do_arquivo += '.mp3'
#         print('Deseja salvar ou apenas reproduzir? ')
#         print('1: Salvar')
#         print('2: Reproduzir')
#         salvar = int(input('Digite 1 para salvar ou 2 para reproduzir '))
        
#         if salvar == 1:
#             print(f' arquivo salvo como {nome_do_arquivo}')
#             texto_audio(texto,nome_do_arquivo)
            
#         elif salvar == 2:
#             texto_audio(texto, 'mp.mp3')

#         continuar = input('Deseja continuar? (Digite "sair" para encerrar): ')
#         if continuar.lower() == 'sair':
#             break
#     except ValueError: 
#         print('Digite um valor inteiro')            





