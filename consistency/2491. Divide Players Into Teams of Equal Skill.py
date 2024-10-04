from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skills  = sorted(skill)
        if len(skills) % 2 != 0: return -1
        left, right = 0, len(skills) - 1
        prev_sum = None
        chemistry = 0
        while left < right:
            pair_sum = skills[left] + skills[right]
            if prev_sum and prev_sum != pair_sum:
                return -1
            chemistry += (skills[left] * skills[right])
            left += 1
            right -= 1
            prev_sum = pair_sum
        return chemistry


if __name__ == '__main__':
    sol = Solution()
    skill = [3, 2, 5, 1, 3, 4]
    skill = [1, 1, 2, 3]
    skill = [3, 4]
    print(sol.dividePlayers(skill))

