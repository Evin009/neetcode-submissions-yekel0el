class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        arr = []
        for val, cnt in count.items():
            arr.append([val,cnt])

        arr.sort(key=lambda x:x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(arr[i][0])
        return res