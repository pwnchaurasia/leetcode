from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        # print('asa', intervals1)
        # intervals.sort(key=lambda x: x[1])
        print(intervals)
        # Step 2: Initialize variables
        count_non_overlapping = 0  # To count non-overlapping intervals
        prev_end = float('-inf')  # Store the end of the last non-overlapping interval
        for start, end in intervals:
            if start >= prev_end:
                count_non_overlapping += 1
                prev_end = end

        return len(intervals) - count_non_overlapping


if __name__ == '__main__':
    sol = Solution()
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(sol.eraseOverlapIntervals(intervals=intervals))