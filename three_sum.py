class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        # Sorting is essential to handle duplicates and use the two-pointer technique
        nums.sort()

        for i in range(len(nums)):
            # If the current pivot number is greater than 0,
            # it's impossible to sum to 0 with numbers to its right
            if nums[i] > 0:
                break

            # Skip the same element to avoid duplicate triplets in the results
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers for the remaining sub-array
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Crucial step: skip duplicate elements for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate elements for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer rightwards
                else:
                    right -= 1  # We need a smaller sum, move right pointer leftwards

        return result


# --- TEST CODE ---
validator = Solution()

financial_balances = [-1, 0, 1, 2, -1, -4]
matched_triplets = validator.threeSum(financial_balances)

print(f"The unique triplets that sum to zero are:\n{matched_triplets}")
# Should output: [[-1, -1, 2], [-1, 0, 1]]