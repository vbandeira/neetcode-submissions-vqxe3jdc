class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = set(nums)
        return len(values) != len(nums)