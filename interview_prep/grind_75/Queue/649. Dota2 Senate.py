from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        for i in range(len(senate)):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        n = len(senate)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r > d:
                dire.append(d + n)
            else:
                radiant.append(r + n)


        return "Radiant" if radiant else "Dire"


if __name__ == '__main__':
    sol = Solution()
    senate = "RDDDDD"
    print(sol.predictPartyVictory(senate=senate))
