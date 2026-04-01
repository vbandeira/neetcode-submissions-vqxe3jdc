class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Iterate over sum
        #   Initialize pointers i+1, len(nums)
        #   While L < R
        #       if sum == 0, save values
        #       if sum > 0, R-1
        #       if sum < 0, L+1
        # Return result
        
        res = set()
        nums.sort()
        for i in range(len(nums)):
            l, r = i+1, len(nums) -1
            while l < r:
                values_sum = nums[i] + nums[l] + nums[r]
                if values_sum == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l, r = l+1, len(nums) -1
                elif values_sum > 0:
                    r -= 1
                else:
                    l += 1
        return list(res)