class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        for index in range (len(first_word)):
            for word in strs[1:]:
                if index >= len(word) or word[index] != first_word[index]:
                    return first_word[:index]
        return first_word
        """
        1. Start with the first word -> firstword = strs [0]
        2. Use a for loop to compare every character in the first word 
        3. Use another for loop to compare every character in every word of   
        the other words...for word in strs[1:], we ignore the first word because we have already covered
        it in the first loop:
        first_word -> bat
        compare
        b     b     b     b
        a     a     a     a
        t     g     n     n
                    k     d

        4. if the indes >= lenght of the word or the words do not match aka
        word[index] != first_word[index]
            4b. then return first_word[:index] aka return the most common words

        5. if all the words match then return the first_word
        """
        

        