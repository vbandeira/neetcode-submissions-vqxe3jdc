class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Iterate over Array    O(n)
        #   Hashmap: Number: Next
        # Iterate over hashmap  O(n)
        #   Check if next exist on Hashmap and count
        #   Mark value as visited

        values = {}
        visited = set()

        for n in nums:
            values[n] = n + 1
        
        maxCount = 0
        count = 1
        for k, v in values.items():
            if k in visited:
                continue
            visited.add(k)
            print(k)
            while v in values:
                visited.add(v)
                count += 1
                v = values[v]
                print('-', v, count)

            maxCount = max(count, maxCount)
            count = 1
        return maxCount