class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else: 
                a = stack.pop()    
                b = stack.pop()    
            
                if token == '+':
                    stack.append(b + a)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':    
                    stack.append(b * a)
                elif token == '/':
                    # returns a float in general    
                    stack.append(int(b / a))
            
        return stack[0]


                                    