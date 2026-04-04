class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # count = {}
        # for i in strs:
        #     count[i[:2]] = 1 + count.get(i[:2], 0)
        
        # arr = []
        # for key, cnt in count.items():
        #     arr.append([key,cnt])
        # arr.sort()

        # long_pair = arr[-1]
        # if long_pair[1] > 1:
        #     return long_pair[0]
        # else:
        #     return ''

        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix



        
