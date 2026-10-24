class Solution:
    def trap(self, height: List[int]) -> int:
        #Output -> total_water (integer)
        #set up everything I need
        left = 0
        right = len(height)-1
        left_max = height[left]
        right_max = height[right]
        total_water = 0
        #while loop
        while left < right:
            #condition to move pointer to left
            if left_max < right_max:
                left += 1
                #calculate total_water
                left_max = max(left_max, height[left])
                #maximum left side - current height
                water_level = left_max - height[left]
                total_water = total_water + water_level



            #condition to move pointer to the right
            elif left_max >= right_max:
                right -= 1
                #calculate total_water
                right_max = max(right_max, height[right])
                water_level = right_max - height[right]
                total_water = total_water + water_level
                
        #return total_water
        return total_water
        