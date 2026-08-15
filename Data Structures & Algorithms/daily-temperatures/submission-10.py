class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temp[i] = daily temp @ ith day
        # return arr - results[i] - no. of days after the 

        ''' 
        temp = [30,38,30,36,35,40,28] : temp[1] = 38 deg on 1st day

        res =  [1,4,1,2,1,0,0] :res[2] = 1 day after day2 temp is 36

        res[i] - no of days after the ith day when the temp increases 

        
        temp = [30,38,30,36,35,40,28]
        stack = [ ]
        res = [30,0,0,0,0,0,0]

        We'll have a stack. The key idea is that we'll start appending elements one by one onto the stack. We'll compare the current element to the top element of the stack and see if the current element is greater than the top element of this stack. If it's not greater than the top element of this stack, we will append that current element onto this stack. Otherwise, we will pop the top element of this stack and calculate the difference of the positions. 
        '''
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                poped_idx = stack.pop() # pop the top value basically its idx
                res[poped_idx] = i - poped_idx # add the difference of the current val and poped_val telling how many dayes it has been
   
            stack.append(i)
        
        return res