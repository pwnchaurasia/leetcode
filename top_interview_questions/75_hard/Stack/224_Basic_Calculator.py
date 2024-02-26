class Solution:
    def calculate(self, s: str) -> int:
        
        operator = {"+", "-", "*", "/"}
        calc_stack = []
        for val in s:
            if val != ")":
                calc_stack.append(val)
            else:
                is_end = True
                small_stack = []
                while is_end:
                    pass









# sol = Solution()
# s = "(1+(4+5+2)-3)+(6+8)"
# sol.calculate(s=s)