class TimeMap:
    # key-val data strcuture
    # store mutiple values for same timestamp
    #retreive key's val at certain timestamp

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # {key - [val, timestamp]}
        if key not in self.hashmap:
            self.hashmap[key] = []
        
        self.hashmap[key].append([value, timestamp])

        # { alice: [ [happy, 1], [sad, 3], [xyx, 5]] }

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key not in self.hashmap:
            return ""
        
        # timestamp exist - return the value associated to it
        # else return the second largest timestamp's val

        arr = self.hashmap.get(key, [])
        
        l = 0
        r = len(arr) - 1

        # sortrd  - binary search
        while l <= r:
            mid = (l + r) // 2

            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                l = mid + 1 # goes up
            else:
                r = mid - 1 # goes left/ lower vals
                
        return res
            
            

