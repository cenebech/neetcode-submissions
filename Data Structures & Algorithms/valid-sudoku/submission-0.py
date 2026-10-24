class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Check Row
        #create 9 rows
        for row in range (9):

            #create a fresh set to store duplicate
            seen = set()

            #create 9 colums to be visited
            for column in range (9):
                #locate the number
                number = board[row][column]
                
                #if it space is empty -> skip it
                if number == ".":
                    continue
                    
                #elif the number is in the seen set then retrun False
                elif number in seen:
                    return False
                    
                #else add it to the seen set
                else:
                    seen.add(number)



        #Check Column - (same moves as rows)
        for column in range (9):
            seen = set()

            for row in range(9):
                number = board [row][column]

                if number == ".":
                    continue

                elif number in seen:
                    return False
                
                else:
                    seen.add(number)



        #Check 3x3

        #1. create a start row process to choose the top, middle, bottom group of boxes (the group
        # ofclass room in each region)
        for start_row in [0,3,6]:

            #2. Create another for loop to choose the left, middle or right box (the class room)
            for start_column in [0,3,6]:
                
                #3. Create a fresh set
                seen = set()

                #for loop to visit the 3 rows
                for row in range (start_row, start_row + 3):
                     #for loop to visit the 3 colums
                     for column in range (start_column, start_column + 3):
                        
                        #locate the number
                        number = board [row][column]
                        
                        #if the spot is empty skip it
                        if number == ".":
                           continue
                        #elif the number is in seen return False
                        elif number in seen:
                            return False
                        # if the number is not it seen then add it
                        else:
                            seen.add(number)


        #return True
        return True





        