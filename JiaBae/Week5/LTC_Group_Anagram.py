from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for str in strs:
            key = ''.join(sorted(str))
            hashmap[key].append(str)

        return list(hashmap.values())