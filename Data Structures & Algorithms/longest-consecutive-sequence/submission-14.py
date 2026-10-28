class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #step 1:
        #Put numbers in a set
        num_set = set(nums)
        longest = 0


        #step 2:
        #Ask for every number is the number behind me here
        #if there is no number behind then it is the start of a sequence
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                count = 1


            #step 3:
            #as long as the current_num+ 1 is in the num_set keep moving
                while current_num + 1 in num_set:
                    #increment the current_num to move forward 
                    current_num += 1
                    #increment the count
                    count += 1

            


                #step 4:
                # find the longest_value
                longest = max(count, longest)

        return longest
  

