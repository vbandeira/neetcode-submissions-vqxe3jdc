class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Upper Bound - O(log n)

        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
        return l -1 if (l and nums[l - 1] == target) else -1