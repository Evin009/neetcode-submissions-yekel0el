class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        - hashmap to keep the count
        - 'AABBACA'
        - keep track of words in each window 
        - (windowLen - max_count <= k) to be valid window
        '''

        hashmap = {}

        l = 0
        max_win = 0

        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            # win_len = r - l + 1
            # max_val = 

            while ((r - l + 1) - max(hashmap.values()) > k):
                hashmap[s[l]] -= 1
                l += 1
                      
            max_win = max(max_win, (r - l + 1))
                
        
        return max_win