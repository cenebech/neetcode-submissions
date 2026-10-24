class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Look at I-pad documentation
        #Step 1: Create three arrays -> create space holders for left, right and answer.
        # remember the space holders are based on the number of elements we have
        n = len(nums)
        left = [1] * n
        right = [1] * n
        answer = [1] * n

        #Step 2: Build the left array
        #we start at position 1 and end at 1
        for i in range(1, n):
            #previous product * previous number on the left/previous position, 
            #remeber if I have no number on the left I use my imaginary 1
            left[i] = left[i-1] * nums[i-1]


        #Step 3: Build the right array
        #we start from second to the last value hence n-2 
        #because the last value has nothing to the right and we put 1 for it
        #we go backwards
        #we stop after index 0
        for i in range (n-2, -1, -1):
            #forward product of right * next value to the right of index
            right[i] = right[i+1]*nums[i+1]


        #Step 4: left x right
        for i in range(n):
            answer[i] = left[i] * right[i]


        #return answer
        return answer