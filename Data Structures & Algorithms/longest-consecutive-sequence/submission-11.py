class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #step 1:
        #Put numbers in a set
        num_set = set(nums)
        current_num = 0
        count = 0
        longest = 0

        #step2:
        #for every number ask -> is the number behind me here:
        # if the number behind is not there then it is the start of a sequence
        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                count = 1



        #Step3 keep checking for the +1 until the number does not exist
            while current_num + 1 in num_set:
                current_num+=1
                count+=1

            longest = max (longest, count)
        return longest




        #Step4
        #count the sequenct
        


        #Step 5 keep the largest length

