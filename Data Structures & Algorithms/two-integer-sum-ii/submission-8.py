class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Binary Search
        for i, n in enumerate(numbers):
            l, r = i + 1, len(numbers)-1
            diff = target - n
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == diff:
                    return [ i + 1, mid + 1]
                if numbers[mid] < diff:
                    l = mid + 1
                    continue
                r = mid - 1
        return []
