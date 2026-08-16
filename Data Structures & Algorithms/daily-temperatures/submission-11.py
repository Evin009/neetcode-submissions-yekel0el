class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ''' 
        temperatures = [30,38,30,36,35,40,28]
        st = [[40, 5], [28, 6]  ]
        38, 1
        res = [1,4,1,2,1,0,0]
        '''

        res = [0] * len(temperatures)
        stack = []

        for idx, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                v, i = stack.pop()
                res[i] = idx - i



            stack.append([val, idx])
        
        return res