class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # string digits: [2,9]
        # each digit from 2-9 mapped to specific char as shown
        # return all possible letter combinations the digit is mapped to  
        # 3 - [d,e,f]; 4 - [g,h,i]
        # base case i >= len(digits) append and return 
        # chose one digit from 3 and one from 4

        digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    #   i          
    # # 34
    #    i        
    # # 34 j = 
    # # d

        if digits == "":
            return []

        res = []

        def dfs(i, cur):
            if i >= len(digits):
                res.append("".join(cur))
                return 
 
            for j in range(len(digitToChar[digits[i]])):
                cur.append(digitToChar[digits[i]][j])
                dfs(i+1, cur)
                cur.pop()

        dfs(0, [])
        return res












