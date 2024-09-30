from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:

            while stack and ast < 0 < stack[-1]:

                if abs(stack[-1]) > abs(ast):
                    ast = 0
                elif abs(stack[-1]) == abs(ast):
                    stack.pop()
                    ast = 0
                else:
                    stack.pop()
            if ast != 0:
                stack.append(ast)
        return stack

if __name__ == '__main__':
    sol = Solution()
    asteroids = [-5, -10, -5, 10, 12, -4, -12, -11]

    print(sol.asteroidCollision(asteroids=asteroids))