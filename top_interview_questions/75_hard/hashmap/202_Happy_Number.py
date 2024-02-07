class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {}
        while n not in visited:
            visited[n] = True
            n = sum([int(i) **2 for i in str(n)])
            if n == 1:
                return True
        return False

    def find_sum(self, n):
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit

            n = n//10
            print(digit, output, n)
        return output

sol = Solution()
n = 19
print(sol.isHappy(n))