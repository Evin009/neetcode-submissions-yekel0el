class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # the value immediate to the left is evaluated needs to be stored and then used ater
        # indicates of stack DS
        '''
        tokens = ["1","2","+","3","*","4","-"]  
        stack = [9,4]
        res. = 5
        '''
        operands = ["+", "-", "*", "/"]

        stack = []

        for val in tokens:
            if val not in operands:
                stack.append(int(val))
            
            else:
                # perfomr the operation on top and the element below it
                ele1 = stack[-1]
                stack.pop()
                ele2 = stack[-1]
                stack.pop()
                if val == "+":
                    num = ele1 + ele2
                elif val == "-":
                    num = ele2 - ele1
                elif val == "*":
                    num = ele1 * ele2
                elif val == "/":
                    num = int(ele2 / ele1)
            
                stack.append(num)
        
        return stack[-1]
            
                