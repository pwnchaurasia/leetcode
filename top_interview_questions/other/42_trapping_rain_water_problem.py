
class Solution:
    def trap(self, height):
        aux_left = []
        aux_right = []
        current_max_left = height[0]
        current_max_right = height[-1]

        for i in height:
            if i >= current_max_left:
                current_max_left = i
            aux_left.append(current_max_left)

        for i in range(len(height)-1, -1, -1):
            if height[i] >= current_max_right:
                current_max_right = height[i]
            aux_right.insert(0, current_max_right)

        trapped_water = 0
        for i in range(len(aux_left)):
            trapped_water += (min(aux_left[i], aux_right[i]) - height[i])
        return trapped_water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
sol = Solution()
print(sol.trap(height))
