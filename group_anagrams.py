from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Using defaultdict(list) guarantees that if a key doesn't exist yet,
        # Python automatically creates an empty list [] for it.
        anagram_groups = defaultdict(list)

        for current_word in strs:
            # 1. Sort the characters of the word to create a unique signature
            # sorted("eat") returns ['a', 'e', 't']
            sorted_characters = sorted(current_word)

            # 2. Join the characters back into a string to use as a dictionary key
            # Python dictionaries require keys to be immutable (strings, tuples, etc.)
            group_key = "".join(sorted_characters)

            # 3. Append the original word to its respective anagram bucket
            anagram_groups[group_key].append(current_word)

        # Return only the grouped values from the dictionary
        return list(anagram_groups.values())


# --- TEST CODE ---
validator = Solution()

word_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
grouped_results = validator.groupAnagrams(word_list)

print(f"Grouped Anagrams:\n{grouped_results}")
# Should output something like: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]