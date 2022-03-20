"""
A hotel manager has to process N advance bookings of rooms for the next season. His hotel has C rooms. 
Bookings contain an arrival date and a departure date. He wants to find out whether there are enough 
rooms in the hotel to satisfy the demand. Write a program that solves this problem in time O(N log N) .
"""

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, k):
        
        n=len(arrive)

        for i in range(n):
            # replace the list elements with tuples where, arrival date
            # will have 'y' along with it and departure date will have 'x'
            # along with it 
            arrive[i]=(arrive[i],'y')
            depart[i]=(depart[i],'x')

        # merge both the lists and sort them
        comb=sorted(arrive+depart)

        for x in comb:
            # If there is an arrival,
            # decrease the available rooms count
            if x[1]=='y':

                # If count reaches 0, no more booking is possible
                if k==0:
                    return 0
                    break
                k-=1

            # If a departure is encounterd
            # increaset the available room count
            else:
                k+=1
        return 1
