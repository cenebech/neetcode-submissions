class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = []
        
        for item in nums:
            if item not in seen:
                seen.append(item)
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
    if item not in seen, then append
    else return True
    return False


    Implement

    '''
        