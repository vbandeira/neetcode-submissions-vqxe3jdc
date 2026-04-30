class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Hash map
        # mp = {i + 1: v for i, v in enumerate(numbers)}
        mp = {}
        
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in mp:
                print(i)
                return [ mp[diff], i + 1]
            mp[n] = i + 1
        return []
