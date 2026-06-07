class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        'cdd'
        '''
        seen = {c,d,}
        '''

        seen = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            length = r - l + 1         
            max_len = max(max_len, length)
        
        return max_len

    