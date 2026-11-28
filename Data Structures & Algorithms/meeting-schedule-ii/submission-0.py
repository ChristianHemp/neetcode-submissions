"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([j.end for j in intervals])

        start_index, end_index = 0, 0
        count, result = 0, 0

        while start_index < len(intervals):
            if start_times[start_index] < end_times[end_index]:
                start_index += 1
                count += 1
                result = max(result, count)
            else:
                end_index += 1
                count -= 1

        return result



        
