class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen_set = set()
        for num in nums:
            if num not in seen_set:
                seen_set.add(num)
            else:
                return True
        return False

        
    '''
    Understand (Input, Ouput, logic)
    Input : list of integers
    Output: boolean -> if any value appears more than once in the array, otherwise return false.

    iterate through the list
    Plan
    create an empty list -> seen
   iterate through the list
   if the item in not in seen -> append
   else:
    return True
    at the end of the loop when all is done return False

    Implement

    '''
    #Alernative solution
    #return len(set(nums)) != len(nums)
        