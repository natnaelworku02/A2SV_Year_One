class TimeMap:

    def __init__(self):
        self.di = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.di[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        val = self.di[key]
        left = 0
        right = len(val) - 1
        ans = -1
        while left <= right:
            mid = (left + right)//2

            if val[mid][0] <= timestamp:
                ans = mid
                left = mid +1
            else:
                right = mid - 1
        return val[ans][1] if ans != -1 else ""


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)