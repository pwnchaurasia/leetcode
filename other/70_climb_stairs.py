class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * (n+1)
        if n < 2:
            return n
        for i in range(n+1):
            if i == 0:
                arr[i] = 0
            elif i == 1:
                arr[i] = 1
            elif i == 2:
                arr[i] = 2
            else:
                arr[i] = arr[i-1] + arr[i-2]
        return arr[-1]


n = 4
ss = Solution()
print(ss.climbStairs(n))
