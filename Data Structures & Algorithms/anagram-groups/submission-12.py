class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # pattern - grouping things (hashmap)
        # need a common key?
        # only lower case letters 
        # brute force - O(m * nlogn)
        # anagrams have same number of elements 

        hashmap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hashmap[tuple(count)].append(s)
        
        return list(hashmap.values())
