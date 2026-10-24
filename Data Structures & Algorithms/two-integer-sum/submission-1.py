class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        for current_index, current_num in enumerate (nums):
            needed_num = target - current_num
            if needed_num in seen_dict:
                return [seen_dict[needed_num], current_index]
            else:
                seen_dict[current_num] = current_index

    '''                       
         Understand (Input, Output, Exaample Edge cases, Logic)
        Input: list of integer -> nums, target = integer
        Output: list of integers -> return the indices i and j such that nums[i] + nums[j] == target


        Edge case: i != j

        Logic:
        iterating through list and adding each number 


        Plan
        -Create and empty seen dictionary -> seen_dict
        - iterate throught the list-> use enumerate to keep track of index and numbers
        - find the number we need that will give us the value of the target
        - to do this we say needed_num = target - current_num
        - check if needed_num is in seen_dict 
                if it is then we return the index of needed_num , index (of current_num)
                else:
                    we store the values in the dictionay
                    seen_dict[current_number] = index

                we use the code in the else statement because If I have not already found the number I 
                need, I have to save my current number so that a future number can use it after the subtraction occurs
                essentially!
                Remember this number and the position where we found it, in case we need it later

        Implement


        '''