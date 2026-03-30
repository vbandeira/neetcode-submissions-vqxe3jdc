class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_idx = {}
        # counter - [(num, count)]
        counter = []
        # iter over nums filling counter
        count_aux = -1
        for n in nums:
            if n not in count_idx:
                count_aux += 1
                count_idx[n] = count_aux
                counter.append((n, 0))
            idx = count_idx[n]
            _, count = counter[idx]
            counter[idx] = (n, count+1)
        # sort by count
        result = sorted(counter, key=lambda x: x[1], reverse=True)
        return [x[0] for x in result[:k]]