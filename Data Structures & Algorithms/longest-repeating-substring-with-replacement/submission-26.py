class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we only shnirk when we can no longer make the replacment
        max_len = 0
        l = 0
        hashmap = {}
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)

            # chkcing the validatity of the replacement
            #keep on shrinking untill the trigger is resolved
            while ( (r-l+1) - max(hashmap.values()) ) > k:
                hashmap[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, (r-l+1))
        
        return max_len