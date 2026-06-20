class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Hash Map to store the most recent index of each character
        char_last_index = {}
        max_length = 0
        left = 0

        # 'right' pointer expands the sliding window character by character
        for right in range(len(s)):
            current_char = s[right]

            # If the character is already in the map and its index is inside
            # our current window, we must shrink the window by moving 'left'
            if current_char in char_last_index and char_last_index[current_char] >= left:
                left = char_last_index[current_char] + 1

            # Update or insert the character's newest position
            char_last_index[current_char] = right

            # Calculate the current window size and update max_length
            current_window_size = right - left + 1
            max_length = max(max_length, current_window_size)

        return max_length


# --- TEST CODE ---
validator = Solution()

stream_data = "abcabcbb"
result = validator.lengthOfLongestSubstring(stream_data)

print(f"The length of the longest substring without repeating characters is: {result}")
# Should output: 3