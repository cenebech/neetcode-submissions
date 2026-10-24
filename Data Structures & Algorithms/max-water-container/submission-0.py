class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #set up everything that I need
        left = 0
        right = len(heights)-1
        largest_area = 0


        #while loop
        while left < right:
            #calculate the area
            #to calculate area = width * height
            #for area, I need width
            #width -> distance from the two bars (right -  left)
            #height is the minimum height because the shoter wall controls our boundary as 
            #water will spill
            
            width = right - left
            wall_height = min(heights[left],heights[right])
            area = width * wall_height
            #find the largest area
            largest_area = max(area, largest_area)

            #condition to move pointer to the left
            if heights[left] < heights[right]:
                left += 1

            #condition to move pointer to the right
            elif heights[left] >= heights[right]:
                right -= 1

        #return largest_area
        return largest_area