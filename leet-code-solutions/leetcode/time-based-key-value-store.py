class TimeMap:

    def __init__(self):
        self.dicto = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dicto[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if self.dicto[key]:
            for i in range(len(self.dicto[key])-1,-1,-1):
                if self.dicto[key][i][1] <= timestamp:
                    return self.dicto[key][i][0]
            return ""
        else:
            return ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)