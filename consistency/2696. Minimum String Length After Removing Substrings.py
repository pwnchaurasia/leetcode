class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            # Check the last character in the stack and the current character
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()  # Remove the last character from the stack
            else:
                stack.append(char)  # Add the current character to the stack

        # The length of the stack is the result
        return len(stack)


if __name__ == '__main__':
    sol = Solution()
    s = "ABFCACDB"
    print(sol.minLength(s=s))