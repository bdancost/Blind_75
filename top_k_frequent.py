class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count the frequency of each number using a Hash Map
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # Step 2: Create the buckets. The index represents the frequency.
        # We need len(nums) + 1 buckets (from 0 to len(nums))
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Populate the buckets based on the frequency
        for num, frequency in counts.items():
            buckets[frequency].append(num)

        # Step 4: Iterate backwards from the highest frequency bucket to collect the top K elements
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                # Once we have collected K elements, we return the result immediately
                if len(result) == k:
                    return result

        return result


# --- TEST CODE ---
validator = Solution()

trending_items = [1, 1, 1, 2, 2, 3]
top_limit = 2

most_frequent = validator.topKFrequent(trending_items, top_limit)
print(f"The top {top_limit} most frequent elements are: {most_frequent}")
# Should output: [1, 2]