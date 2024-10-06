from bisect import bisect_left


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort the potions to enable binary search
        potions.sort()

        # Initialize the result list
        result = []

        # Loop through each spell
        for spell in spells:
            # Calculate the minimum potion strength needed for a successful pair
            required_strength = (success + spell - 1) // spell  # To handle rounding up

            # Use binary search to find the first potion that meets the required strength
            idx = bisect_left(potions, required_strength)

            # Count the number of successful pairs by subtracting the index from the total potions
            result.append(len(potions) - idx)

        return result