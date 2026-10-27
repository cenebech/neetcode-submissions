class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Input - List
        #Output - sublists of 3 numbers when added their sum result to zero
        #Edge cases: list is empty,there a alpaphets in list, non of the sum results to 0

        #core logic : 2 pointers
        
        #set up everthing that I need

        #sort num
        nums.sort()

        #initialize empty list that will contain final result to be returned
        result = []

        #for loop - we want to ensure that we leave 2 numbers at the end for pathners
        for index in range(len(nums)-2):


            #First check to avoid duplicates:
            #if the value is a the first index or the next values are not the same we continue
            #Imagine you are going down a list of people’s requests. If two people in a row request the
            #same thing, you only need to do that work once. 
            if index == 0 or nums[index] != nums[index-1]:

                #move pointers to the location
                left = index + 1
                right = len(nums)-1

                #while loop
                while left < right:
                    ##add the values
                    total = nums[index] + nums[left] + nums[right]

                    #elif our total is smaller then move left pointer forward
                    if total < 0:
                        left += 1

                    #elif out total is larget then move righ pointer backwards
                    elif total > 0:
                        right -= 1


                    #else if our number is exactly zero! yay! then we  append the values to result
                    else:
                        result.append([nums[index],nums[left], nums[right]])

                        #we keep looking for more tripletes
                        #move left pointer
                        left += 1

                        #move right pointer
                        right -= 1

                        #Second check for pointer on the left
                        while left < right and nums[left] == nums[left-1]:
                            left += 1


                        #Third check for pointer on the right
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
        return result




     