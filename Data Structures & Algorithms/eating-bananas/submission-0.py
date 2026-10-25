class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right


        while left <= right:
            k = (left + right)//2

            total_hours = 0

            #for loop for hours
            for pile in piles:
                
                #calculate hoursPerPile
                hoursPerPile = math.ceil(pile/k)

                #update total hours
                total_hours += hoursPerPile


            #check that total hours is not past the deadline -> h
            if total_hours <= h:
                #assign to our output variable
                result = k
                    
                #can I do better? can I eat slower -> move right pointer back
                right = k - 1


            #else
            elif total_hours > h:
                    
                #move left pointer forward
                left = k + 1


        return result


        