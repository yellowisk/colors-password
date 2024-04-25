# MC102 - Projeto 1

Neste projeto, vocês irão projetar a estratégia do jogo **Senha** (*code* ou *guess the code*), em duplas.
Vocês irão implementar a tomada de decisão do jogador e utilizar as funções já prontas para interagir com o jogo.


## O Jogo

Neste jogo existe uma senha de quatro cores (entre sete cores no total, sem repetição) e seu objetivo é adivinhar a senha.
Para isso, vocês podem chutar uma certa senha e o jogo lhes dirá duas informações: quantas cores das que vocês chutaram estão na senha e quantas estão na posição correta.
Vocês possuem um total de 10 tentativas para acertar.

Vamos ver um exemplo. Observe o chute abaixo:

    (1): 🟦 🟨 🟥 🟧  => (2, 1)

Nele, testamos a combinação &ldquo;azul, amarelo, vermelho e laranja&rdquo; e o jogo nos disse que, dentro dessas 4 cores, 2 estão presentes na senha e 1 está na posição correta.
Perceba que, uma cor que está na posição correta, irá contar tanto para o número de cores presentes e o número de posições corretas.

Nosso próximo chute pode ser:

    (2): 🟦 🟧 🟥 ⬜  => (2, 2)

Tiramos o amarelo e inserimos o branco, mas a quantidade de cores não mudou. Ou o amarelo está na senha e o branco também ou nenhum dos dois estão.

Além disso, o número de cores em posições corretas subiu. Quais informações podemos tirar disso?

O jogo termina quando vocês acertarem a senha ou quando vocês atingirem o número máximo de tentativas (por padrão, 10). No exemplo acima, o código correto era:

    Correct: 🟦 🟩 🟨 ⬜


## O Código

Todo o código deste projeto está dentro da pasta `src`.
**Vocês só deve alterar o arquivo** `player.py`.

Uma breve descrição do que cada arquivo faz:

-   **main.py:** contém a entrada ao projeto. É este arquivo que deve ser chamado (`python3 src/main.py`) e ele vai decidir quais arquivos precisam ser usados.
-   **colors.py:** contém o código para as cores. Existem 7 variáveis que vocês podem usar para representar as cores e elas são definidas lá no final deste arquivo.
-   **codes.py:** contém as funções de checagem da senha.
-   **terminal.py:** contém a interface de terminal do jogo.
-   **game.py:** contém a interface gráfica do jogo.
-   **interactive.py** contém a lógica de inserção de cores pelo terminal.
-   **player.py:** irá conter a lógica do seu jogador.

Vocês não precisam entender 100% desses outros arquivos, mas sintam-se à vontade para dar uma lida.
**Não os altere, apenas o player.py**.


## Como executar

A principal forma de executar este projeto é utilizando o comando:

    python3 src/main.py

Por padrão, ele tentará abrir a interface gráfica que utiliza a biblioteca `pygame`. Vocês podem instalá-la utilizando o comando:

    pip3 install --user pygame

Caso tenha problemas para fazer essa instalação, confira com algum monitor.

Caso não queira utilizar a interface gráfica, vocês podem utilizar o terminal rodando o projeto pelo seguinte comando:

    python3 src/main.py -t

Caso queira jogar o jogo diretamente, pode utilizar o comando
    
    python3 src/main.py -t -i
    
e escrever as cores desejadas.

## As Regras

1.  Vocês não devem alterar o código dos outros arquivos além do `player.py`. Vocês podem criar mais arquivos, caso prefiram, mas não é necessário.
2.  Vocês não devem &ldquo;roubar&rdquo; nas regras do jogo: não vale olhar o valor da variável, burlar a contagem de chutes, alterar a escolha da senha a ser adivinhada etc&#x2026;


## Para submeter

Vocês devem entregar seu projeto pelo Google Classroom, compactando toda a pasta em um único arquivo `.tar.xz` ou `.zip`. Vocês devem compactar a pasta do projeto e não somente o `src/`.

**O nome do arquivo comprimido deve conter os RAs da dupla separados por um *underline*.** Exemplo: `123456_123456.tar.xz`.

## Performance esperada

O seu código não precisa ser o mais rápido do mundo, nem o mais preciso do mundo. Mas ele ainda sim precisa ser melhor do que chutar aleatóriamente. Ou seja, acertar mais do 10 em 840 (1.19%).

Além disso, esperamos que haja um "esforço genuíno" no desenvolvimeento de alguma estratégia. **Tem que haver alguma estratégia**.

Qualquer dúvida se a sua estratégia está "boa o suficiente" procure um PED e pergunte a respeito.

## Avaliação

Como dito acima, seu código não será avaliado na performance, mas sim na qualidade deste. Desta forma, ele deve conter:
- a definição de ao menos uma função (além da `player`).
- chamada de uma outra função.
- um laço (while ou for).
- comparações e condicionais.
- construção e acesso de listas.

Além disso, o código deve aderir a todas as convenções, normas e boas práticas de código que vimos no curso até hoje.

## Torneio

Quandos todas entregas forem submetidas, iremos utilizar o código no arquivo `tournament.py` para rodar seu código diversas vezes e obter o percentual de acertos. As três submissões com melhores percentuais terão a nota das listas anteriores aumentadas conforme a seguinte regra:
- 1º lugar: equivalente a nota máxima de 1.5 listas
- 2º lugar: equivalente a nota máxima de 1   lista
- 3º lugar: equivalente a nota máxima de 0.5 lista

Além disso, os ganhadores receberão o maior prêmio de todos: um parabéns e aperto de mão.
