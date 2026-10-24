class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        for index in range (len(first_word)):
            for word in strs[:]:
                if index >= len(word) or word[index]!= first_word[index]:
                    return first_word[:index]

        return first_word
        

        