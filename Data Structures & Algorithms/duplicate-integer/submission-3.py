class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = set(nums)
        return len(values) != len(nums)
        
        # values = set()
        # for n in nums:
        #     if n in values:
        #         return True
        #     values.add(n)
        # return False