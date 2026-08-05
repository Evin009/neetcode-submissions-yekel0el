class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given - arr of string
        # what to do - group all anagrams in a list and store all the lists onto a list
        # return - list of lists

        # duplicates - yes
        # null - yes 
        # no anagrams - yes return a sublist

        # jubmled letters in a word 
        # can we sort the letter - yes we can 
        # add sorted letters onto a hasmap
        # sorted version - letter

        hashmap = {}

        # we need a key for all grouping a common key 
        # here common key is the sorted strings

        for s in strs:
            sorted_s = tuple(sorted(s))
            if sorted_s not in hashmap:
                # create a key-list pair
                hashmap[sorted_s] = []
            hashmap[sorted_s].append(s)
        
        res = []
        for val in hashmap.values():
            res.append(val)
        
        return res



        