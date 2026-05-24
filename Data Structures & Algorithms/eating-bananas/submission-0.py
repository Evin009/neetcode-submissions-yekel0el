class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles[h] num of bananas in the ith pile
        # piles =  [1,4,3,2] -> piles[2] = 3 bananas in 2nd pile
        # h = number of hours to eat all bananas
        # k = bananas/hour eating rate
        # each hour - choose a pile and eat k bananas 

        # if pile[i] < k = finish eating the pile but cannot eat from other pile

        #RETURN - min 'k' to all bananas in 'h' hours

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2 
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res