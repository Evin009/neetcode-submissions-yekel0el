class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        - s null return ""
        - t null return ""
        - s has duplicate value of t: we only care about the count of elements in t once the t elements count goes down start shiernking
       
        * count of all the t elements needs to be in substring to be valid
        '''
        if len(s) < len(t):
            return ""

        count_t = {}
        for i in t:
            count_t[i] = 1 + count_t.get(i, 0)
        
        res = [-1, -1]
        resLen = float('inf')

        need = len(count_t) # all the elemetns needs to be in 
        have = 0

        # the substring should have all the t element count
        count_s = {}

        l = 0
        for r in range(len(s)):
            # keep on adding till the count of t is filled
            # either add all elements and chk if the element that is present has its count filled
            count_s[s[r]] = 1 + count_s.get(s[r], 0)

            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                have += 1
            
            # we start shirnk when need = have
            while need == have:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                count_s[s[l]] -= 1

                # if the count of required element goes below the needed value 
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                
                l += 1

        l, r = res
        return s[l: r + 1]




            