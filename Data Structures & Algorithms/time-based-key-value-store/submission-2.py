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
        for i in self.hash_map[key]:
            if i[1] <= timestamp:
                res = i[0]
            else:
                break
        return res