class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        curr_interval = intervals[0]

        for i in range(1, len(intervals)):
            # interval entirely before next
            if curr_interval[1] < intervals[i][0]:
                result.append(curr_interval)
                curr_interval = intervals[i]
            # intervals overlap
            else:
                curr_interval = [
                    min(curr_interval[0], intervals[i][0]),
                    max(curr_interval[1], intervals[i][1])
                ]
        
        result.append(curr_interval)
        
        return result