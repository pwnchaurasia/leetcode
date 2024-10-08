from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  # Initialize the result array with 0s
        stack = []  # Stack to store indices of the temperatures array

        # Traverse the temperatures list
        for i in range(n):
            # Check if the current temperature is higher than the temperature of the day at the stack's top index
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()  # Get the index of the previous colder day
                answer[prev_day] = i - prev_day  # Calculate the number of days to a warmer day

            # Push the current day's index onto the stack
            stack.append(i)

        return answer


if __name__ == '__main__':
    sol = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(sol.dailyTemperatures(temperatures=temperatures))
