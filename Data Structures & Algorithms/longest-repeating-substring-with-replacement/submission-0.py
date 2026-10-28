class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        """

        left = 0
        longest = 0
        count = {}

        #when invalid move left
        #when valid move right

        #for loop -> moves right pointer:
            #frequency map

            

            #While loop -> check validity of my window
            #While loop -> total lenght of values - values that we have > k
            #While loop -> window - max count.values() > k
            #grocceries in basket example
                #remove something


            left += 1


            #calculate window
            #compare maximu values of the longest


        #return longest

        """
        left = 0
        longest = 0
        count = {}

        for right in range (len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            
            #while basket/total available replacement > k ($10):
                #remove the item from basket
            while (right-left+1) - max(count.values()) > k:
                count[s[left]] -= 1

                left += 1

            window = (right - left) + 1
            longest = max(longest, window)

        return longest

            

        