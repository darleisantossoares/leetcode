## DAG - Direct Acyclic Graph

Um DAG é um grafo que não tem nenhum ciclo.

Vamos continuar com o mesmo exemplo do algoritmo fibonacci

Cada chamada é um nós do nosso DAG

Quando estamos no nó 6 (ou chamada da função com o parametro 6) esse mesmo nó se conecta com o nó 5 e 4, o 5 se conecta com o 4 (mesmo nó) e 3, e a lista continua...
Usando esta lógica, conseguimos ver um relacionamento entre os nós e um DAG

Usar um DAG fica mais simples de identificar *subproblems* e *overlapping subproblems* .

No exemplo abaixo conseguimos ver essa relação.

![image](https://user-images.githubusercontent.com/5891902/179262754-082117e4-fc59-4d07-ad7b-e0b5f1b9a166.png)

## Como resolver quase todo problema com DP

Normalmente DP pode se aplicar para problemas de optimização. Então se um problema quer encontrar o menor/maior ou mínimo/máximo, normalmente o problema pode se resolver com DP.
Para problemas de DP tente sempre encontrar as duas sub estruturas.

- Optimal Substructure
- Overlapping Subproblems

Para tentar encontrar a recorrencia em um problema, siga os passos.:

1. Entenda os problema
2. Imagine que alguém te dá a resposta para os subproblemas
3. Encontre a relação entre os subproblemas
4. Tente quebrar os subproblemas no menor tamanho possível




