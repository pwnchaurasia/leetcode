from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort(key= lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = output[-1][1]
            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
        
        return output







sol = Solution() 
intervals = [[1,3],[6,9]]
newInterval = [2,5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(sol.insert(intervals=intervals, newInterval=newInterval))