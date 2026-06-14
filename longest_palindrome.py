class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_sub = ""

        # Helper function to expand outwards from a given center
        def expand_around_center(left: int, right: int) -> str:
            # Expand while pointers are within bounds and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the valid palindromic substring found
            # (Note: left+1 because the loop stops after shifting one step too far)
            return s[left + 1: right]

        for i in range(len(s)):
            # Case 1: Odd length palindromes (e.g., "aba", center is 'b')
            odd_palindrome = expand_around_center(i, i)
            if len(odd_palindrome) > len(longest_sub):
                longest_sub = odd_palindrome

            # Case 2: Even length palindromes (e.g., "abba", center is "bb")
            even_palindrome = expand_around_center(i, i + 1)
            if len(even_palindrome) > len(longest_sub):
                longest_sub = even_palindrome

        return longest_sub


# --- TEST CODE ---
validator = Solution()

dna_sequence = "babad"
result = validator.longestPalindrome(dna_sequence)

print(f"The longest palindromic substring is: {result}")
# Should output: "bab" (or "aba")