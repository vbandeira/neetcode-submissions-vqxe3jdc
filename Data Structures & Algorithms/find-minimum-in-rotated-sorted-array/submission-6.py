class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Minha solução: O(log(n))
        l, r = 0, len(nums) - 1
        ans = nums[0]
        
        while l <= r:
            # If array is sorted, get the left element 
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break

            # Calculate mid and update answer if needed
            mid = l + ((r - l) // 2)
            ans = min(ans, nums[mid])

            # If left portion is sorted, move left pointer
            # Else, move the right pointer
            # Equality needed to handle single element lists
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return ans
            
            