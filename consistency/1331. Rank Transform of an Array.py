from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)

        # Step 2: Assign ranks using a hash map
        rank_map = {}
        rank = 1
        for num in sorted_arr:
            if num not in rank_map:  # Only assign rank to first occurrence
                rank_map[num] = rank
                rank += 1

        # Step 3: Replace original array elements with their rank
        return [rank_map[num] for num in arr]




if __name__ == '__main__':
    sol = Solution()
    # arr = [40, 10, 20, 30]
    arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    print(sol.arrayRankTransform(arr=arr))
