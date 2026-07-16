class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Time: O(N) - Space: O(1)
        slow, fast = 0, 0

        while slow != fast or slow == 0:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow