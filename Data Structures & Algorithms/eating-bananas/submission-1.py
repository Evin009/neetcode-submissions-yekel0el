class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles[i] - num of bananas in the ith pile
        # piles = [1,4,3,2]; piles[1] = 4 bananas in 1st pile
        # h = num of hours to eat all bananas
        # k - banana-per-hour eating rate

        # each hour chose a pile and eat k banana from pile
        # if pile has less than k banana, finish the pile only

        # return min k - to eat all bananas in h hours
        
        ''' 
        piles = [1,4,3,2] h = 9
        total_b = 10
        k = 1 : 10 hours to eat > h
        k = 2 : 6 hours to eat < h (min k)
        k = 3 : 5 hours < h

        min it will take len(piles) hours to eat all the bananas
        h >= len(piles) else not possible
        max it will take sum of all the bananas
        # time: min - len(piles); max: sum of piles
        this is the possible time for eating bananas 4 <= h <= 10

        if eating at rate of k bananas/hr
        - ceil(x/k) hr to eat x pile inside the piles arr
        if k = 1; 1/1 = 1, 4/1 = 4, ...
        k = 2; 1/2 = 1, 4/2 = 2, 3/2 = 2, 2/2 = 1 : total - 6hr < 9

        time : len(piles) < h < sum(piles)
        => 4 < h < 10
        => k (min) = 1; k (max) = max(piles[i]) 4
        => 1 < k < 4
        => k min whcih does in h < 9
        => use binary search to find a k - calulcate the total_ time: ceil(x/k) if time < 9 shrink range else expand

        '''

        # bianry search on hthe ans pattern
        k_min = 1
        k_max = max(piles) 
        # k_arr = []
        # k = [1,2,3,4]
        # for i in range(k_min, k_max+1):
        #     k_arr.append(i)
        
        l, r = 1, k_max # 1 - 25
        res = r # (k - max but takes min time)

        while l <= r:
            k = (l + r) // 2 # k = 13

            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i] / k) # time > h
            
            
            if time <= h: # time > h
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1 # l = 14
        
        return res

            


