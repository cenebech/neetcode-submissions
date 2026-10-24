class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers)-1

        #while loop
        while left < right:
            #current_sum = left + right
            current_sum = numbers[left] + numbers[right]
            
            #if current_sum == target:
            if current_sum == target:
                #return [left+1, right+1]
                return [left+1, right+1]
                
            #elif current number is smaller > terget:
            elif current_sum < target:
                left += 1
                
            else:
                right -= 1

        
         
            
        