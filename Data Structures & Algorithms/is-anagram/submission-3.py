class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make hashmap of all the char in both the words 
        # if both the hasmaps are same return true

        hashmap_1 = {}
        hashmap_2 = {}

        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            hashmap_1[s[i]] = 1 + hashmap_1.get(s[i], 0)
            hashmap_2[t[i]] = 1 + hashmap_2.get(t[i], 0)

        if hashmap_1 == hashmap_2:
            return True
        
        return False
        