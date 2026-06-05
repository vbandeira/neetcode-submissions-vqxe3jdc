class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Minha solução: O(log n)

        L, R = 0, len(nums) - 1
        breakpoint = -1

        # if len(nums) == 1:
        #     return 0 if nums[0] == target else -1

        # Find the sorted array which might contain target
        while L <= R:
            mid = (L + R) // 2
            if mid < len(nums)-1 and nums[mid + 1] < nums[mid]:
                breakpoint = mid
                break
            
            if nums[L] < nums[mid]:
                L = mid + 1
            else:
                R = mid - 1

        if breakpoint < 0:
            breakpoint = len(nums) - 1
        
        L, R = 0, len(nums) - 1

        # Binary search over previous array
        if nums[L] <= target and target <= nums[breakpoint]:
            L = 0
            R = breakpoint
        else:
            L = breakpoint + 1
            R = len(nums) - 1

        print(L, R, breakpoint)

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1
        
        return -1
