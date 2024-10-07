from bisect import bisect_left
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort the potions to enable binary search
        potions.sort()
        len_potions = len(potions)

        # Initialize the result list
        result = []

        # Loop through each spell
        for spell in spells:
            # Calculate the minimum potion strength needed for a successful pair
            required_strength = (success + spell - 1) // spell  # To handle rounding up

            # Use binary search to find the first potion that meets the required strength
            idx = bisect_left(potions, required_strength)

            # Count the number of successful pairs by subtracting the index from the total potions
            result.append(len_potions - idx)

        return result


if __name__ == '__main__':
    sol = Solution()
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    print(sol.successfulPairs(spells=spells, potions=potions, success=success))