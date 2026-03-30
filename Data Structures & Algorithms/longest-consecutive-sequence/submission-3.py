class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        longest = 0

        for val in values:
            if (val -1) not in values:
                length = 1
                while (val + length) in values:
                    length += 1
                longest = max(longest, length)
        
        return longest