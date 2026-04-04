class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freqency = hashmap
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        # [val, cnt]
        arr = []
        for key, cnt in hashmap.items():
            arr.append([key,cnt])
        
        # sorting [val, cnt] but based on 'cnt' 
        arr.sort(key=lambda x:x[1], reverse=True)

        # append first k 'val' in res
        res = []
        for i in range(k):
            res.append(arr[i][0])
        
        return res