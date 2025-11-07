from collections import deque

class Solution:
    def count_min(self, intervals: List[List[int]]) -> int:
        q = deque(intervals)
        count = 0
        while q:
            start, end = q.popleft()
            temp_q = deque()
            count += 1
            for _ in range(len(q)):
                curr_s, curr_e = q.popleft()
                if end <= curr_s:
                    start, end = curr_s, curr_e
                else:
                    temp_q.append((curr_s, curr_e))
            q = temp_q
        return count

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:        
        if len(intervals) == 1:
            return 1
        
        intervals_end = sorted(intervals, key=lambda x: x[1]) # sorting on end times
        intervals_start = sorted(intervals)
        return min(self.count_min(intervals_start), self.count_min(intervals_end))
        


