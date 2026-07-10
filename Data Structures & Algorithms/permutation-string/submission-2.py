class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #s1 in s2 in any order - T
        # len(s1) > len(s2) - F

        if len(s1) > len(s2):
            return False

        left = 0
        # window size 
        win_size = len(s1)

        # letter count of s1
        count_s1 = {}
        for i in range(win_size):
            count_s1[s1[i]] = 1 + count_s1.get(s1[i], 0)
        
        # check if letter count within a window of size - win_size is same as count_s1 - True

        count_s2 = {}

        for right in range(len(s2)):
            # checking if win_size greater then skrink
            if (right - left + 1) > win_size:
                # if letter count 1 remove from hashmap of s2
                if count_s2[s2[left]] == 1:
                    del  count_s2[s2[left]]
                else:
                    # decresing the letter count in s2 hashmap
                    count_s2[s2[left]] -= 1    
                left += 1
            
            # adding letter and its count in s2 hashmap
            count_s2[s2[right]] = 1 + count_s2.get(s2[right], 0)

            if count_s1 == count_s2:
                return True
        return False 
                