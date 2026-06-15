class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Alternativa 1: Contar intervalos necessários

        # Contar a frequência de cada tarefa
        freq = Counter(tasks)
        # Ordena valores da frequencia
        freqSorted = sorted(freq.values())
        # Obtem maior frequencia
        maxF = freqSorted[-1]
        # Calcular o espaço inicial de slots
        idle = (maxF -1) * n
        # Para cada outra tarefa com contador:
        for i in range(len(freqSorted)-2, -1, -1):
        #   Decrementa o espaço inical de slots com o menor 
        #   valor entre a maior frequência -1 e a tarefa
            idle -= min(maxF -1, freqSorted[i])
        # Se houverem espaços, soma ao tamanho de tasks.
        # Se não, retorna o tamanho de tasks
        return max(0, idle) + len(tasks)