from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        c1 = {}
        c2 = {}
        char_diff = 0

        for i in range(len(s)):
            c1[s[i]] = c1.get(s[i], 0) + 1
            c2[goal[i]] = c2.get(goal[i], 0) + 1

            if s[i] != goal[i]:
                char_diff += 1
                if char_diff > 2:
                    return False

        if c1 != c2:
            return False

        for num_count in c1.values():
            if num_count >= 2:
                return True

        if char_diff < 2:
            return False
        return True


if __name__ == '__main__':
    sol = Solution()

    s = "ab"
    goal = "ba"

    print(sol.buddyStrings(s=s, goal=goal))

    s = "aa"
    goal = "aa"

    print(sol.buddyStrings(s=s, goal=goal))