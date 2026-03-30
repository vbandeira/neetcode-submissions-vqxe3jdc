class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        arr = []
        for n, cnt in count.items():
            arr.append([cnt, n])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])    # pop pega último elemento, sem precisar reverter o array
        return res