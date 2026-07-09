class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        hashset = set()
        max_len = 0

        for right in range(len(s)):

            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1

            hashset.add(s[right])

            length = right - left + 1
            max_len = max(length, max_len)

        return max_len