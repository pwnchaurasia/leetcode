from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = deque()
        di = deque()

        next_position = len(senate)
        for i in range(len(senate)):
            if senate[i] == 'R':
                rad.append(i)
            else:
                di.append(i)
        print(rad)
        print(di)
        while rad and di:
            if rad[0] < di[0]:
                rad.append(next_position)
            else:
                di.append(next_position)
            rad.popleft()
            di.popleft()
            next_position += 1
        return "Radiant" if rad else "Dire"


sol = Solution()
senate = "RD"
print(sol.predictPartyVictory(senate=senate))