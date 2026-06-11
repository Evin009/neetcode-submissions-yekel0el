class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        - hashmap to keep the count
        - 'AABBACA'
        - keep track of words in each window 
        - (windowLen - max_count <= k) to be valid window

        -'ABCD' k = 1
        {A: 1, B : 1,  C: 1, D: 1} l = 0 , r = 1
        size = 1 (1 - 1 > 1) F
        r = 1, size = 1 (2 - 1 > 1) F
        r = 2, (3 - 1 > 1) T, l = 1--> {B : 1,  C: 1, D: 1}
        ()
        '''

        hashmap = {}

        l = 0
        max_win = 0

        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            ''' wrong - window length does not change later - make sure condition changes'''
            # win_len = r - l + 1
            # max_val = max(hashmap.values()

            while ((r - l + 1) - max(hashmap.values()) > k):
                hashmap[s[l]] -= 1
                l += 1
                      
            max_win = max(max_win, (r - l + 1))
                
        
        return max_win