class TimeMap:

    def __init__(self):
        self.hashtable = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashtable:
            self.hashtable[key] = []
        
        self.hashtable[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashtable:
            return ""
        
        result = ""
        for val, time in self.hashtable[key]:
            if time <= timestamp:
                result = val
            else:
                break
        return result

