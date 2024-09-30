from inspect import stack


class Solution:
    def decodeString(self, s: str) -> str:
        stack_str = []
        stack_num = []
        curr_str = ""
        curr_num = 0
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == "[":
                stack_str.append(curr_str)
                stack_num.append(curr_num)
                curr_str = ""
                curr_num = 0
            elif char == "]":
                repeat_num = stack_num.pop()
                prev_str = stack_str.pop()
                curr_str = prev_str + curr_str * repeat_num
            else:
                curr_str += char
        return curr_str



if __name__ == '__main__':
    sol = Solution()
    s = "3[a]2[bc]"
    print(sol.decodeString(s=s))
