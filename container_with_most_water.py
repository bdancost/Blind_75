class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water_area = 0

        # Move pointers inward until they meet
        while left < right:
            # Calculate width and height of the container
            width = right - left
            current_height = min(height[left], height[right])

            # Update the maximum area found so far
            current_area = width * current_height
            max_water_area = max(max_water_area, current_area)

            # The key logic: always move the pointer pointing to the shorter bar,
            # because only a taller bar can potentially increase the area.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water_area


# --- TEST CODE ---
validator = Solution()

height_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = validator.maxArea(height_list)

print(f"The maximum amount of water that can be contained is: {result}")
# Should output: 49