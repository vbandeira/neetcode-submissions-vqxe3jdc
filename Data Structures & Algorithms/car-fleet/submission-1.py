class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        fleet_count = 1
        p, s = pair[0]
        prev_time = (target - p) / s

        for i in range(1, len(pair)):
            p, s = pair[i]
            curr_time = (target - p) / s
            if curr_time > prev_time:
                fleet_count += 1
                prev_time = curr_time
        return fleet_count