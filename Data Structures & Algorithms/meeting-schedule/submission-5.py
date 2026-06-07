"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        max_interval_dex = 0
        max_interval_length = 0
        max_interval_start = 0
        max_interval_end = 0
        
        for i in range(len(intervals)):
            length = intervals[i].end - intervals[i].start
            if length >= max_interval_length:
                max_interval_length = length
                max_interval_dex = i
                max_interval_start = intervals[i].start
                max_interval_end = intervals[i].end
        
        for i in range(len(intervals)):
            if i != max_interval_dex:
                if intervals[i].start == max_interval_start and intervals[i].end == max_interval_end:
                    return False
                if intervals[i].start > max_interval_start and intervals[i].start < max_interval_end:
                    return False
                if intervals[i].end > max_interval_start and intervals[i].end < max_interval_end:
                    return False
        
        return True