class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Pointers for the binary search
        left = 0
        right = len(nums) - 1

        # Binary Search loop
        while left < right:
            mid = (left + right) // 2

            # If middle element is greater than the rightmost element,
            # the minimum must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum is in the left half (including mid).
            else:
                right = mid

        # When left == right, we've found the minimum element
        return nums[left]


# --- TEST CODE ---
validator = Solution()

# Rotated sorted array: [4, 5, 6, 7, 0, 1, 2]
rotated_data = [4, 5, 6, 7, 0, 1, 2]
min_value = validator.findMin(rotated_data)

print(f"The minimum element found is: {min_value}")
# Should output: 0