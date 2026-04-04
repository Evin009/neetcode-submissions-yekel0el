class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Count_map = {}
        for item in strs:
            sorted_item = tuple(sorted(item))
            if sorted_item not in Count_map:
                Count_map[sorted_item] = []
            Count_map[sorted_item].append(item)

        result = []
        for value in Count_map.values():
            result.append(value)
        return result
            