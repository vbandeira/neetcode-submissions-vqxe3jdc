class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        

        pre = [1] * (len(nums))        # Product before index
        post = [1] * (len(nums))       # Product after index
        aux_pre = 1     # Accumulator for product before index
        aux_post = 1    # Accumulator for product after index

        for i in range(len(nums)-1):
            aux_pre *= nums[i]
            aux_post *= nums[-i-1]
            pre[i] = aux_pre
            post[-i-1] = aux_post

        res = []
        print(pre, post)
        for i in range(len(nums)):
            tmp_pre = pre[i-1] if i >= 0 else 1
            tmp_post = post[i+1] if i+1 < len(post) else 1
            # print(i, tmp_pre, tmp_post)
            res.append(tmp_pre * tmp_post)
        return res