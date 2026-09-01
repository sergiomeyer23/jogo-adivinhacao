# 🎯 Jogo de Adivinhação em Python

Um jogo simples de linha de comando onde o computador sorteia um número entre 1 e 100, e o jogador precisa adivinhá-lo com o menor número de tentativas possível, usando dicas de "maior" ou "menor".

## 📋 Sobre o projeto

Este projeto foi desenvolvido como parte dos meus estudos de lógica de programação em Python. O objetivo foi praticar:

- Estruturas de repetição (`while`)
- Estruturas condicionais (`if` / `elif` / `else`)
- Validação de entrada do usuário
- Manipulação de listas (histórico de tentativas)
- Recursão (rejogar automaticamente ao final da partida)
- Números aleatórios com o módulo `random`

## 🚀 Como executar

Pré-requisito: ter o Python 3 instalado.

```bash
python jogo_adivinhacao.py
```

## 🎮 Como jogar

1. O programa sorteia um número secreto entre 1 e 100.
2. Digite um número inteiro como palpite.
3. O jogo informa se o palpite foi muito alto ou muito baixo.
4. Continue tentando até acertar o número.
5. Ao final, veja quantas tentativas você usou e o histórico de palpites.
6. Escolha se quer jogar novamente.

## 🧠 Exemplo de execução

```
==============================================
     JOGO DE ADIVINHAÇÃO EM PYTHON
==============================================
Pense em um número de 1 a 100.
Tente adivinhar qual é!

Seu palpite: 50
Muito alto! Tente um número MENOR.

Seu palpite: 25
Muito baixo! Tente um número MAIOR.

Seu palpite: 37
Parabéns! Você acertou em 3 tentativas.
Seus palpites foram: [50, 25, 37]

Quer jogar de novo? [s/n]
```

## 🔧 Próximas melhorias

- [ ] Refatorar para orientação a objetos (classe `JogoAdivinhacao`)
- [ ] Adicionar níveis de dificuldade (faixas de números diferentes)
- [ ] Salvar histórico de partidas em arquivo
- [ ] Adicionar contagem de tempo por partida

## 🛠️ Tecnologias

- Python 3

## 👤 Autor

Sérgio Meyer — https://github.com/sergiomeyer23

Projeto feito como parte da minha jornada de aprendizado em programação, migrando de uma área comercial/operacional para desenvolvimento de software.