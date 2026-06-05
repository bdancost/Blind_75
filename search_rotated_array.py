class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Standard Binary Search loop
        while left <= right:
            mid = left + (right - left) // 2

            # If we found the target, return its index immediately
            if nums[mid] == target:
                return mid

            # CASE 1: The left half is perfectly sorted
            if nums[left] <= nums[mid]:
                # Check if the target lies within this sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Shrink to the left side
                else:
                    left = mid + 1  # Target must be on the right side

            # CASE 2: The right half must be perfectly sorted
            else:
                # Check if the target lies within this sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Shrink to the right side
                else:
                    right = mid - 1  # Target must be on the left side

        return -1  # Target was not found in the array


# --- TEST CODE ---
validator = Solution()

rotated_indices = [4, 5, 6, 7, 0, 1, 2]
search_target = 0

result_index = validator.search(rotated_indices, search_target)
print(f"The target {search_target} is located at index: {result_index}")
# Should output: 4