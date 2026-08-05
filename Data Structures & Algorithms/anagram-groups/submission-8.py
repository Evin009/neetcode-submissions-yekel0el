class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for item in strs:
            sorted_item = tuple(sorted(item))
            if sorted_item not in hashmap:
                hashmap[sorted_item] = []
            hashmap[sorted_item].append(item)
    
        res = []
        for value in hashmap.values():
            res.append(value)
    
        return res