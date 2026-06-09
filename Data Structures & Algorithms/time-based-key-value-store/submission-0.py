# Busca binária

class TimeMap:

    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.values[key]
        res = ''
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            v, t = values[mid]
            if t <= timestamp:
                l = mid + 1
                res = v
            else:
                r = mid - 1
        return res

