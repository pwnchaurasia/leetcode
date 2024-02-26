from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                first = stack.pop()
                second = stack.pop()
                if token == "+":
                    val = second + first
                elif token == "-":
                    val = second - first
                elif token == "*":
                    val = second * first
                elif token == "/":
                    val = int(second / first)
                stack.append(val)

        return stack[0]









sol = Solution()
tokens = ["2","1","+","3","*"]
tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = ["10","6","-132","/","*","17","+","5","+"]
print(sol.evalRPN(tokens=tokens))