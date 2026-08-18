class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create a hasmap to store position and its time
        # if position of A < position of B and time A < time B: A and B will form a fleet
        # if position A < position B and time A > time B: A and B will not form fleet

        position_sorted = []

        for idx, val in enumerate(position):
            position_sorted.append([val, speed[idx]])

        '''
        p = [ [7,1] , [4,2] , [1,2] ,[0,1] ] time_prev >= time - pop
        t = 10 - 0 / 1 = 10 
        stack = [3, ]
        '''
        
        position_sorted.sort(reverse=True)

        stack = []
        count = 0
        for car in position_sorted:
            time = (target - car[0]) / car[1]

            stack.append(time)
            
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()


        return len(stack)



