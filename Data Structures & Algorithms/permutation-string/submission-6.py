class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = defaultdict(int)

        for c in s1:
            s1_map[c] += 1

        need = len(s1_map)
        for i in range(len(s2)):
            s2_map, cur = defaultdict(int), 0
            # Cur -> Contador de caracteres iguais em ambos os hashmaps

            for j in range(i, len(s2)):
                s2_map[s2[j]] += 1

                if s1_map[s2[j]] < s2_map[s2[j]]:
                    break
                if s1_map[s2[j]] == s2_map[s2[j]]:
                    cur += 1
                if need == cur:
                    return True
        return False    
            