class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            chars = sorted(s)
            groups.setdefault(str(chars), []).append(s)
        return [x for x in groups.values()]