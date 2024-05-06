from collections import deque
from queue import Queue


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1
        queue = Queue()
        queue.put((startGene, 0))
        visited = {startGene}
        while not queue.empty():
            gene, steps = queue.get()
            if gene == endGene:
                return steps

            for i in range(len(gene)):
                for c in 'ACGT':
                    new_gene = gene[:i] + c + gene[i+1:]
                    if new_gene not in visited and new_gene in bank:
                        visited.add(new_gene)
                        queue.put((new_gene, steps+1))
        return -1
