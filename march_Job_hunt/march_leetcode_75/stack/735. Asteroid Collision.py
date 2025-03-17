from collections import deque
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return list(stack)



if __name__ == "__main__":
    asteroids = [5, 10, -5]
    # asteroids = [8, -8]
    # asteroids = [10, 2, -5]

    sol = Solution()
    res = sol.asteroidCollision(asteroids=asteroids)
    print(res)