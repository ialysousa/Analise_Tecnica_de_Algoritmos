:pencil2: 1. Dados os pesos e valores de N itens, coloque esses itens em uma mochila de capacidade W para obter o máximo valor total na mochila. 

Em outras palavras, dadas duas matrizes inteiras val[0..N-1] e wt[0..N-1] que representam valores e pesos associados a N itens, respectivamente. 

Dado também um inteiro W que representa a capacidade da mochila, descubra o valor máximo do subconjunto de val[] de modo que a soma dos pesos desse subconjunto seja menor ou igual a W. 

Você não pode quebrar um item, pegar o item completo ou não escolha (propriedade 0-1).

Exemplo:

Entrada: N = 3, W = 4

valores[] = {1,2,3}

peso[] = {4,5,1}

Saída: 3

Entrada: N = 3, W = 3

valores[] = {1,2,3}

peso[] = {4,5,6}

Saída: 0

-----------------------
:pencil2: 2. Dada uma haste de comprimento n polegadas e uma matriz de preços que inclua os preços de todas as peças de tamanho menor que n. 

Determine o valor máximo obtido cortando a haste e vendendo os pedaços. 

Por exemplo, se o comprimento da haste for 8 e os valores das diferentes peças forem dados como a seguir, o valor máximo obtido é 22 (cortando em duas peças de comprimentos 2 e 6). 

comprimento | 1 2 3 4 5 6 7 8  

preço | 1 5 8 9 10 17 17 20

E se os preços forem os seguintes, o valor máximo obtido é 24 (cortando em oito pedaços de comprimento 1) 

comprimento | 1 2 3 4 5 6 7 8  

preço | 3 5 8 9 10 17 17 20

------------------------

:pencil2: 3. Implemente o algoritmo LCS de 3 formas:

a. Algoritmo recursivo

b. Algoritmo recursivo memoizado top-down

c. Algoritmo com PD (bottom-up)

