class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n, 'b')
        n = n.zfill(32)

        return int(n[::-1], 2)


sol = Solution()
n = "00000010100101000001111010011100"
print(sol.reverseBits(n=int(n)))


