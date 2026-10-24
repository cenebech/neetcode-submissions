class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check the length of the strings
        if len(s) != len(t):
            return False

        return sorted (s) == sorted (t)
        
        #create dictionationary to store the counters 

        