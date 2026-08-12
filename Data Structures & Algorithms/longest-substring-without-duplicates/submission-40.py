class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # substring continous = sliding window
        # dynamic sliding window
        # keep on pdating the sldiding window
        # shrink only if the element is seen

        seen = set()

        if len(s) == 0:
            return 0
        
        max_length = 0

        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])

            length = r - l + 1
            max_length = max(max_length, length)

        return max_length



        