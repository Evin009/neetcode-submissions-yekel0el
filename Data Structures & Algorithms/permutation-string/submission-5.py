class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        # fixed length sliding window
        win_size = len(s1)

        count_s1 = {}
        for i in range(len(s1)):
            count_s1[s1[i]] = 1 + count_s1.get(s1[i], 0)
        
        l = 0
        count_s2 = {}
        for r in range(len(s2)):
            # shrink window size if it exeeded the win_size
            if (r-l+1) > win_size:
                # when shrinking remove the element left is point to if the count of it is 1 delete it from the hashmap
                if count_s2[s2[l]] == 1:
                    del count_s2[s2[l]]
                
                else:
                    # decrement
                    count_s2[s2[l]] -= 1

                l += 1
            

            count_s2[s2[r]] = 1 + count_s2.get(s2[r], 0)
        
            if count_s2 == count_s1:
                return True
        
        return False