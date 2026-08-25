class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # split and check for palindrome
        # 'aab' - first split 
    #       i  
    # #    'AAB'
    #       j
        # cur = [a,a]
        # choices cut can have this word or not
        # run an index when the idex == len(s) return 

        res = []
    
        def dfs(start_idx, cur):
            if start_idx >= len(s):
                res.append(cur.copy())
                return
            
            for j in range(start_idx, len(s)):
                # chose and check
                if self.isPalindrome(s[start_idx:j+1]):
                    cur.append(s[start_idx:j+1])
                    dfs(j + 1, cur)
                    cur.pop()
        dfs(0, [])
        return res


    def isPalindrome(self, string):
        start = 0
        end = len(string) - 1
        while start <= end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        
        return True


