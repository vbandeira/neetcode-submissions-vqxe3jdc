class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Alternativa 2: Matemática

        # A tarefa com a maior frequência determina o mínimo 
        # necessário do agendamento;
        # Se uma tarefa aparece maxF vezes, as cópias serão
        # separadas por pelo menos n intervalos, criando (maxF - 1) 
        # intervalos com duração de (n + 1);
        #
        # Então o tempo mínimo necessário é:
        #   (maxF - 1) * (n + 1) + maxCount
        #   onde maxCount é a quantidade de tarefas com a mesma
        #   frequência máxima

        # Calcula frequência
        freq = Counter(tasks)

        # Pega maior frequência
        maxF = max(freq.values())

        # Conta quantas tarefas tem a maior frequência
        maxCount = sum([1 for i in freq if freq[i] == maxF])

        # Calcula o tempo mínimo
        time = (maxF - 1) * (n+1) + maxCount

        # Retorna o maior valor entre a quantidade de tarefas e 
        # o tempo mínimo.
        return max(len(tasks), time)