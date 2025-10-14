# Trabalho_Ordenacao_Grupo42

### Trabalho 02 - 13/10/2025

## Alunos  
| Matrícula | Nome |  
|-----------------------|---------------------|  
| 18/0113097 | Daniel Coimbra dos Santos |  

## Descrição do projeto
Resolução de questões do LeetCode para demonstrar na prática os conhecimentos adquiridos acerca do conteúdo Algoritmos de Ordenação

### Questão de Dificuldade Média:
#### 969. Pancake Sorting
Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[0...k-1] (0-indexed).
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= arr.length
All integers in arr are unique (i.e. arr is a permutation of the integers from 1 to arr.length).


## Capturas de tela
<img src="[Runtime](/imgs/pancakeSorting.PNG)"><br>
<img src="[Questão e código](/imgs/runtime_pancakesorting.PNG)"><br>

## Conclusões
Este algoritmo funciona em pelo menos 4 etapas:
1. Encontra o maior número não-ordenado.
2. Gira o array para que o número fique em frente.
3. Então Gira novamente para que vá para a posição correta no final.
4. Repete até que todos os números estejam ordenados

Complexidade:
      Tempo: O(n²) -> Porque cada pesquisa e reversão pode tomar até n passos.
      Espaço: O(1) extra (ordena no próprio array), mais O(n) para a lista do resultado

**Pontos fortes**: Simples, in-place, garantia de funcionamento, bom para fins didáticos.
**Pontos fracos**: Lento (O(n²)), não é prático para grande volume de dados, pode usar mais giros do que o mínimo necessário. 

É um problema combinatório, e com capacidade de abstração interessante

## Referências
O algoritmo de Ordenação por Panquecas (Pancake Sorting) foi inventada por Jacob E. Goodman, que apresentou o problema pela primeira vez em 1975 sob o pseudônimo "Harry Dweighter". O problema foi posteriormente publicado em um influente artigo de 1979 pelo fundador da Microsoft, Bill Gates, e por Christos Papadimitriou, que desenvolveram um algoritmo eficiente para resolvê-lo.

Jacob E. Goodman: Matemático que criou o problema por volta de 1975 enquanto empilhava toalhas, comparando o processo com a ordenação de panquecas de diferentes tamanhos, invertendo seções da pilha. Inicialmente, ele enviou o problema para o American Mathematical Monthly.

Bill Gates: Quando era estudante de graduação, coautorizou um artigo significativo com Christos Papadimitriou intitulado "Bounds for Sorting by Prefix Reversal", que apresentou um algoritmo eficiente para a ordenação por panquecas e foi publicado em 1979. Esse algoritmo foi o mais eficiente por muitos anos.

## Grupo
<img src="https://avatars.githubusercontent.com/u/49206670?s=400&u=200e3dc888a00aa86108318d2d9b6c33aa94abe1&v=4" width=150><br>
      <b><a href="https://github.com/DanielCoimbra">Daniel Coimbra</a></b><br>
