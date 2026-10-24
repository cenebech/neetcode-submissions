class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #1. frequency map
        count_dict = {}
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1

        #2. Create buckets

        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])


        #3. Fill values in buckets
        for num in count_dict:
            frequency = count_dict[num]
            bucket[frequency].append(num)


        #4. Find the top K elements by going backwards

        result  = []
        for frequency in range(len(bucket)-1,0,-1):
            for num in bucket[frequency]:
                result.append(num)

            
            if len(result) == k:
                return result
        '''
        1. Step 1:
        Create the frequency map. Map all numbers to their freguency
        example: [1,1,2,3,3,4,4,4,7,7,7,7]
        In this case 
        1 = 2
        2 = 1
        3 = 3
        4 = 3
        7 = 4 

        This just basically means that:
        1 shows up 2 times
        2 shows up 1 times
        3 shows up 2 times
        4 shows up 3 time
        7 shows up 4 times

        2. Step 2 -> for efficiey reasons we will create a bucket, so that 
        all the values that show up X amountof times will be placed in that 
        bucket

        e.g 
        bucket [1] = 2 (bucket [1] hold all the values that show up once, \
        in this case 2 shows 
        up once )
        bucket [2] = [1,2] (only 1 is the value/number that show up once)
        bucket [3] = [4] -> 4 shows up 3 times which is why it is in buc
        bucket [4] = [7]

        3. Step 3:
        Fill the bucket with the values
        bucket [2] = [1,2] (only 1 is the value/number that show up once)
        bucket [3] = [4] -> 4 shows up 3 times which is why it is in buc
        bucket [4] = [7]  

        4. Step 4:

         a. create an empty list -> result where we will store all the top k 
         elemenets
         b. read the values backwards from the bucket because we know that
         the bcket will have top values saved backwards
         e.g 
        bucket [2] = [1,2]
        bucket [3] = [4] 
        bucket [4] = [7]  

        the top values are :
        bucket [3] = [4] 
        bucket [4] = [7] 

        because they are at the bottom

        c. another for loop to go and iterate every single number inside 
        the bucket
        d. append the most frequent numbers inside the result
        e. print the result




        '''
        