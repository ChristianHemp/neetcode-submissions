from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.hash_map = defaultdict(list[tuple])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map:
            return ""
        
        values = self.hash_map[key]
        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        return values[right][0] if right >= 0 else ""
