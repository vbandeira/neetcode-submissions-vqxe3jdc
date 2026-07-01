class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        in_degree = defaultdict(int)

        for w in words:
            for c in w:
                in_degree[c] = 0

        for i in range(len(words) -1):
            w1 = words[i]
            w2 = words[i + 1]

            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ''

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break
        

        q = deque([k for k,v in in_degree.items() if v == 0])

        result = []

        while q:
            c = q.popleft()
            result.append(c)
            for n in graph[c]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    q.append(n)
        
        return ''.join(result) if len(result) == len(in_degree) else ''