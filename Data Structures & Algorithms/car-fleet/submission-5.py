class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # need to find how many fleet of cars?

        # to become a fleet-        
            # single car considered a fleet
            # if two or more cars reach at destination at same time they are cosidered as a fleet

        # car in behind - if catches up it goes at same speed as ususal cannot speed up or overtake
        # it means if car behind travel time less than or equal to car ahead travel time they will become fleet

        # p = [1,4,2,8,5] -> [8,5,4,2,1]
        # s = [2,2,3,2,5] -> [2,5,2,3,2]
        # t = 10 -> d = [2,5,6,8,9]; t = [1,1,3,2.6,4.5] - fleet = 2  

        # cars_speed = {}

        # for i in range(len(position)):
        #     cars_speed[position[i]] = speed[i]

        # position_sorted = position.sort(reverse=True) #sort in descending order
        # sorted_speed  = []

        # for i in range(len(position_sorted)):
        #     if position_sorted[i] in cars_speed:
        #         sorted_speed.append(cars_speed[position_sorted[i]])
        
        # sorted_speed and 
        
        cars = list(zip(position, speed))
        stack = []

        cars.sort(reverse=True)
        # p = [1,4,2,8,5] -> [8,5,4,2,1]
        # s = [2,2,3,2,5] -> [2,5,2,3,2]
        # t = 10 -> d = [2,5,6,8,9]; t = [1,1,3,2.6,4.5] - fleet = 2  

        for pos, spd in cars:
            time = (target - pos) / spd
            
            stack.append(time)

            # if time <= stack[-1]:
            #     stack.pop()
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

        




            


