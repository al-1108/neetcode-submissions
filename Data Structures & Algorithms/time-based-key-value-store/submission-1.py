class TimeMap:
    def __init__(self):   
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append([value, timestamp])
        else:
            self.map[key] = [[value, timestamp]]       

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        l, r = 0, len(self.map[key])-1
        res = ""
        while l <= r:
            m = l + (r-l) // 2
            if self.map[key][m][1] <= timestamp:
                res = self.map[key][m][0]
                l = m+1
            else:
                r = m-1
        return res

        #bin search timestamp till find, if not find, take lower bound timestamp
        
