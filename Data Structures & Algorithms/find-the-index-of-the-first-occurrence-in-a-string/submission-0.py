class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #check that the haystack is less than needle
        if len(haystack) < len(needle):
            return -1

        #create the window
        window = len(needle)

        #create where we want our window to end
        latest_start = len(haystack) - len(needle)

        #create our for loop
        for start in range(latest_start +1):
            #check contents in the window by grabbing a piece
            piece = haystack[start:start+window]
            
            #check that our piece is the same as needle
            if piece == needle:
                #return the index of first occurance of needle
                return start


           


        return -1


        
        