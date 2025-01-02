class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Define vowels
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Helper function to check if a word starts and ends with a vowel
        def is_vowel_string(word):
            return word[0] in vowels and word[-1] in vowels

        # Precompute prefix sums for words that satisfy the condition
        prefix = [0] * (len(words) + 1)
        for i, word in enumerate(words):
            prefix[i + 1] = prefix[i] + (1 if is_vowel_string(word) else 0)

        # Answer the queries using the prefix sums
        result = []
        for li, ri in queries:
            result.append(prefix[ri + 1] - prefix[li])

        return result
