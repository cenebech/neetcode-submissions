class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagram_group:
                anagram_group[sorted_word] = [word]
            else:
                anagram_group[sorted_word].append(word)

        return list(anagram_group.values())
        """
        Understand
        Input: list of strings
        Output: list of string that  group all anagrams together into sublists



        Plan
        create an empty dictionry -> anagram_group
        iterate throught the dictionry:
        for word in strs:
            #seperate each word, sort and glue it back together
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagram_group:
                anagram_group[sored_word] = [word]
            else:
                anagram_group[sorted_word].append
        return list(anagram_group.values())




        Implement



        """
        