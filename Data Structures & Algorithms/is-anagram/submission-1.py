class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}

        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1

        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1

        return s_dict == t_dict



        '''
        Understand (Input, Output, Example, Edges/contrains, Logic)

        Input: two strings "s" and "t"
        Ouput: Boolean values -> return true if the two strings are anagrams of each other, 
        otherwise return false

        Example :
        Done

        Logic:
        Iterate through the list

        Edge case: The lenghth of "s" and "t" have to be the same



        Plan
        1. Check the length of "s" and " t" and return False if they not the same
        2. return a sorted boolean value comparing s and t
        



        Implement


       


        
        Understand:




        Plan
        check if the lenght of s and t are the same, if they are not return false

        create empty doctionary for s
        create empty dictionary for t

        #keep track of all the values in s

        if char not in s:
            s_dict[char] = 1
        else:
            s_dict[char] += 1

        #keep track of all the values in t
        if char not in t:
            s_dict[char] = 1
        else:
            s_dict[char] += 1

        return s_dict == t_dict

        # #ALTERNATIVE SOLUTIONS USING DICTIONARIES
        # if len(s) != len(t):
            #return False
        # return sorted(s) == sorted(t)

      
'''















        