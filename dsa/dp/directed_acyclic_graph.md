## DAG - Direct Acyclic Graph

Um DAG é um grafo que não tem nenhum ciclo.

Vamos continuar com o mesmo exemplo do algoritmo fibonacci

Cada chamada é um nós do nosso DAG

Quando estamos no nó 6 (ou chamada da função com o parametro 6) esse mesmo nó se conecta com o nó 5 e 4, o 5 se conecta com o 4 (mesmo nó) e 3, e a lista continua...
Usando esta lógica, conseguimos ver um relacionamento entre os nós e um DAG

Usar um DAG fica mais simples de identificar *subproblems* e *overlapping subproblems* .

No exemplo abaixo conseguimos ver essa relação.

![image](https://user-images.githubusercontent.com/5891902/179262582-5eaf5a2a-e82d-4554-af3b-e215aa2bffbe.png)






