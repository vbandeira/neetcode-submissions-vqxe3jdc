class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Binary Search
        for i, n in enumerate(numbers):
            print(i,n)
            diff = target - n
            l, r = i + 1, len(numbers)-1
            while l < r:
                mid = (l + (r - l)) // 2
                if numbers[mid] == diff:
                    return [ i + 1, mid + 1]
                if numbers[mid] < diff:
                    l = mid
                r = mid
        return []