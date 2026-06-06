class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Hash Map to store the character frequencies
        char_counts = {}

        # Count frequencies in the first string
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1

        # Subtract frequencies using the second string
        for char in t:
            # If a character from 't' is not even in 's', it's not an anagram
            if char not in char_counts:
                return False
            char_counts[char] -= 1

        # If all counts are zero, it's a perfect anagram
        for count in char_counts.values():
            if count != 0:
                return False

        return True


# --- TEST CODE ---
validator = Solution()

word_one = "anagram"
word_two = "nagaram"

is_match = validator.isAnagram(word_one, word_two)
print(f"Are '{word_one}' and '{word_two}' anagrams? {is_match}")
# Should output: True