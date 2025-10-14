from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        """Ordena a matriz usando giros de panqueca e retorna os tamanhos dos giros."""
        flips = []
        n = len(arr)

        # Ordena até o segundo menor elemento
        for size in range(n, 1, -1):
            # Encontre o índice do maior número atual
            max_index = arr.index(size)

            # Pula se já estiver no lugar correto 
            if max_index == size - 1:
                continue

            # Passo 1: Gira para trazer o maior número para o início
            if max_index != 0:
                flips.append(max_index + 1)
                arr[:max_index + 1] = reversed(arr[:max_index + 1])

            # Passo 2: Gira para mover para a posição final
            flips.append(size)
            arr[:size] = reversed(arr[:size])

        return flips
