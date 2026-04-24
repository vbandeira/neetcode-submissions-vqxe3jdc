class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Deque

        res = []
        l = 0
        q = collections.deque() # Only indices

        for r in range(len(nums)):
            # Remove values smaller than r from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # Add value to deque
            q.append(r)

            # Remove value from q if is not in window
            if q[0] < l:
                q.popleft()

            # Check if window if valid
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
        
        return res
            
