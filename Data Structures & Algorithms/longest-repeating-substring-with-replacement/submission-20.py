class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # need to get the count 
        # if a letter has less count replace that
        # {A:3, B: 1}
        # total_words - max_freq <= k expand the window     
        letter_count = {}
        left = 0
        max_freq = 0
        max_win = 0

        for right in range(len(s)):
            letter_count[s[right]] = 1 + letter_count.get(s[right],0)
            # finding the letter with max freq
            max_freq = max(max_freq, letter_count[s[right]])
            
            while ((right - left + 1) - max_freq) > k:
                letter_count[s[left]] -= 1
                left += 1
            
            max_win = max(right-left+1, max_win)

        return max_win

            