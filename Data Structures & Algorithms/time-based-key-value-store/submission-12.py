class TimeMap:

    def __init__(self):
        # self.pairs = {"alice" : {1 : "happy", 3: "sad"}}
        self.pairs: dict[str, dict[int, str]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if len(self.pairs.get(key, {})):
            self.pairs[key][timestamp] = value
        else:
            self.pairs[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.pairs: return ""

        if self.pairs[key].get(timestamp, "") != "":
            return self.pairs[key][timestamp]

        self.timestamp_prev = -1
        timestamps = list(self.pairs[key].keys())

        def bs(front, end):
            if front > end: return ""
            mid = (front + end) // 2
            mid_timestamp = timestamps[mid]

            if timestamp == mid_timestamp:
                self.timestamp_prev = -1
                return self.pairs[key][mid_timestamp]
            if timestamp > mid_timestamp:
                self.timestamp_prev = mid_timestamp
                return bs(mid + 1, end)
            if timestamp < mid_timestamp:
                return bs(front, mid - 1)
        
        value = bs(0, len(timestamps) - 1)

        if value != "": return value
        if self.timestamp_prev != -1: return self.pairs[key][self.timestamp_prev]
        
        return ""

