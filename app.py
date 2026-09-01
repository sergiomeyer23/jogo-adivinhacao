"""
JOGO DA ADIVINHAÇÃO
O computador sorteia um número avulso de 1 a 100.
Seu objetivo: descobrir o número com o menor número de tentativas possivel.
As dicas mostram se seu palpite ficou MUITO ALTO ou MUITO ABAIXO. Boa sorte!
"""

import random

def jogar():
    # Executa uma rodada completa do jogo de advinhacao

    numero_secreto = random.randint(1,100)
    tentativas = 0
    historico = []

    print("Pense em um número de 1 a 100.")
    print("Tente adivinhar qual é!\n")

    # O loop continua até o jogador acertar o número
    while True:
        entrada = input("Seu palpite: ")

        # Garante que a entrada é um número inteiro válido.
        if not entrada.isdigit():
            print("Digite apenas números inteiros!")
            continue

        palpite = int(entrada)
        tentativas += 1
        historico.append(palpite)

        if palpite < numero_secreto:
            print("Muito baixo! Tente um número MAIOR.\n")
        elif palpite > numero_secreto:
            print("Muito alto! Tente um número MENOR.\n")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            print(f"Seus palpites foram: {historico}\n")
            break

    # Oferece uma nova rodada ao final do jogo
    resposta = input("Quer jogar de novo? [s/n]")
    if resposta.lower().startswith("s"):
        jogar()


# Ponto de entrada do programa
if __name__ == "__main__":
    print("="*46)
    print("     JOGO DE ADIVINHAÇÃO EM PYTHON")
    print("="*46)
    jogar()