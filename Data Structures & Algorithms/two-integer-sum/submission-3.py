class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for i in range(len(nums)):
            values.setdefault(nums[i], []).append(i)
        
        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in values:
                for j in values[diff]:
                    if i != j:
                        return [i,j]

        