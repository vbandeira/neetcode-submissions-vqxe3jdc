class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Complexities: Time: O(C) where C is the number of chars
        #               Space: O(V+E) because of graph
        
        graph = defaultdict(set)
        in_degree = defaultdict(int)

        # Creates in degree for all chars
        for w in words:
            for c in w:
                in_degree[c] = 0

        # Iterate over words comparing it to the next
        for i in range(len(words) -1):
            w1 = words[i]
            w2 = words[i + 1]

            min_len = min(len(w1), len(w2))
            # Edge case: If first word is bigger than second but they have the same content
            #   case is invalid
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ''

            # Iterate over possible chars
            for j in range(min_len):
                if w1[j] != w2[j]:
                    # If char on second word is not related to char on first one,
                    #   add it to graph and increment its in_degree.
                    # This avoids duplicate edges on repeated patterns.
                    # It is possible to add to graph after the if, because
                    #   it is a hashset.
                    
                    if w2[j] not in graph[w1[j]]:
                        in_degree[w2[j]] += 1
                        graph[w1[j]].add(w2[j])
                        
                    break
        

        # Kahn's Algorithm
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