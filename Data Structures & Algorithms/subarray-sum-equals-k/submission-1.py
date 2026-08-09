class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # given - list of ints, sum of subarray - k
        # what to do - subarray, contiguous we need to find them which adds up to k
        # return - count of contiguous subarray non empty whose sum is k

        '''
        COnstrains: Zeroes ? Y, Negetives - Y , duplitcates - Y

        '''

        '''
        - as we working on subarrays: can we use sliding window ? - No as negetives are allowed 
        - we are concereed with sum of subaarys so prefix sum
        - prefix sum[j] - prefix sum[i - 1] = k or cur_sum - prefix_sum = k (sum of subarray/ subarray itself)
        - so we need to look for prefix sum which can be subtracted from cur sum which can give us subarray
        - now the specific prefix sum we are looking form is cur_sum - k = prefix sum: store that we see so far 

         |-----|   
        [2, 1, 1, 2] k = 2 {0 : 1, 2 : 1, 3 : 1, 4 : 1} (prefix : count)
        cur_sum = 0
        i = 0, cur_sum = 0 + 2 = 2( 2- 2 = 0) (yes in hash count = hash[0] = 1 update hash)
        i = 1, cur_sum = 0 + 2 + 1 = 3 (3 - 2 = 1) (Not in hash update hash)
        i = 2, cur_sum = 0 + 2 + 1 + 1 = 4 (4 - 2 = 2) (seen count = hash[2] = 1 and update the hash)
        i = 3, cur_sum = 4 + 2 = 6 (6 - 2 = 4)(seen hash[4] = count = 1)

        count = 3 ([2], [1,1], [2])
        '''
        count = 0
        prefix_hash = {0:1} # default 
        cur_sum = 0
        prefix_sum = 0

        for i in nums:
            cur_sum += i
            # finding the needed prefix sum to look for subarray with sum k
            prefix_sum = cur_sum - k
            
            # checking if req prefix sum in hash if yes update count else add the cur sum onto as prefix seen
            if prefix_sum in prefix_hash:
                count += prefix_hash[prefix_sum]
            
            prefix_hash[cur_sum] = 1 + prefix_hash.get(cur_sum, 0)
        
        return count
        