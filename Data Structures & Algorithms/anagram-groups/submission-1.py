class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string in hashmap:
                hashmap[sorted_string].append(s)
            else:
                hashmap[sorted_string] = [s]
        return list(hashmap.values())