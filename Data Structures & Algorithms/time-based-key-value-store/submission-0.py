class TimeMap:

    def __init__(self):
        self.dct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dct:
            self.dct[key].append([timestamp, value])
        else:
            self.dct[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dct:
            return ''

        records = self.dct[key]
        l = 0 
        r = len(records) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2

            if records[mid][0] <= timestamp:
                result = records[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return result