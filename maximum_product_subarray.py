class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # All variables initialized in English using the first element
        current_max = nums[0]
        current_min = nums[0]
        global_max = nums[0]

        # Iterating through the list starting from the second element
        for i in range(1, len(nums)):
            current_num = nums[i]

            # Critical detail: if the current number is negative,
            # the maximum possible value becomes the minimum, and vice versa.
            # So, we swap current_max and current_min values.
            if current_num < 0:
                current_max, current_min = current_min, current_max

            # At each step, we calculate the new extremes comparing:
            # 1. The number by itself (starting a new subarray)
            # 2. The number multiplied by the previous accumulated value
            current_max = max(current_num, current_max * current_num)
            current_min = min(current_num, current_min * current_num)

            # Updating our definitive global answer
            global_max = max(global_max, current_max)

        return global_max


# --- TEST CODE ---
validator = Solution()

growth_rates = [2, 3, -2, 4, -3]
# Testing flow: 2*3 = 6 -> 6*-2 = -12 -> -12*4 = -48 -> -48*-3 = 144!
# Notice how the negative numbers cancelled out at the end and generated a huge value.

highest_multiplier = validator.maxProduct(growth_rates)
print(f"The maximum product subarray is: {highest_multiplier}")
# Should output: 144