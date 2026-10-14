class TimeMap:

    def __init__(self):
        self.hash_map = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map:
            return ""
        res = ""
        l,r = 0, len(self.hash_map[key]) - 1
        while l <= r:
            mid = (l+r)//2
            if self.hash_map[key][mid][1] <= timestamp:
                res = self.hash_map[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res