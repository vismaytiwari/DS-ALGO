class TimeMap:
    import bisect
    def __init__(self):
        '''
        dic = {
        "key":
            [list,dict2()]
        }
        '''  
        self.dic = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.dic.get(key):
            arr  = self.dic[key]
            arr[0].append(timestamp)
            arr[1][timestamp] = value
            self.dic[key] = arr
        else:
            self.dic[key] = [[timestamp],{timestamp:value}]
    def get(self, key: str, timestamp: int) -> str:
        if key in self.dic:
            if timestamp in self.dic[key][1]:
                return self.dic[key][1][timestamp]
            else:
                x = bisect.bisect_left(self.dic[key][0],timestamp)
                # print(timestamp,x,self.dic)
                if x == 0 :
                    return ""
                return self.dic[key][1][self.dic[key][0][x-1]]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)