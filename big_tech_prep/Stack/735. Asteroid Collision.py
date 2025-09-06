class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for aster in asteroids:
            while stack and aster < 0 < stack[-1]:
                if abs(aster) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(aster) == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(aster)
        return list(stack)


