
from time import sleep
import os

secreto = 'perfume'.upper()
digitadas = []
tentativas = 3
jogo = 'JOGO DA FORCA'





print('=' * 60)
print(F'{jogo:^60}')
print('=' * 60)


while True:
                ############ RECEBENDO AS LETRAS E AS VERIFICANDO
    letra = input('Digite uma letra: ').upper()

    if len(letra) > 1 or letra == '':
        print('Digite Apenas uma Letra !!!.')
        continue

    digitadas.append(letra)
                ####### CASO A LETRA DIGITADA ESTEJA PRESENTE NA PALVRA SECRETA
    if letra in secreto:
        print()
        print(f'Uhuuu, a letra {letra} existe na palavra secreta.')
    else:
        print()
        print(f'Aff, a letra nao existe na palava secreta.')
        digitadas.pop()

              ######## LISTA DAS LETRAS QUE FORMAM A PALAVRA
    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

            ##########  CASO O USUARIO ACERTE A PALAVRA OU PERCA SUAS CHANCES
    if secreto_temporario == secreto:
        print()
        print(f'Voce ganhou !!!! A palavra é {secreto.upper()}')
        sleep(2)


            ###### STATUS DA PALAVRA
    else:
        print(f'A palavra secreta esta assim: {secreto_temporario}')

            ############ CASO O JOGADOR ERRE A LETRA
    if letra not in secreto:
        tentativas -= 1

            ######## CHANCES DO JOGADOR
    if tentativas != 0 :
        print(f'Restam {tentativas} chances.')

    else:
        print(f'Voce nao tem mais tentativas.')

    if tentativas == 0:
        print()
        print('Voce perdeu!!!')
        sleep(2)


    if tentativas == 0 or secreto_temporario == secreto:
        os.system('cls') or None
        ficha = str(input('Deseja jogar novamente [S/N] : ')).upper().strip()
        if ficha == 'S':
            digitadas.clear()
            tentativas = 0
            tentativas += 3
        else:
            print('Fechando o jogo ...')
            sleep(2)
            break







