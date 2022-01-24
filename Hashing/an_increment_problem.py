"""
Given a stream of numbers A. On arrival of each number, you need to increase its first occurence by 1 and include this in the stream.

Return the final stream of numbers.
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        hash_map = {}

        # Start iterating through each number
        for i,num in enumerate(A):

            # If num not in hash_map then store it as key,
            # with value being the list containing the indexes
            # where that num is present
            if num not in hash_map:
                hash_map[num] = [i]

            else:
                # If it is in the hash_map, check if value list is empty or not
                if len(hash_map[num]) > 0: 
                    # If not empty, then take the index of first occurece ..it will always be on pos 0,
                    # since we will sort the indexes, whenever we add them in the list
                    first_occ_idx = hash_map[num][0]
                    
                    # remove this index from the list
                    hash_map[num] = hash_map[num][1:]

                    # Increase its value by 1
                    A[first_occ_idx] += 1

                    # If the new number after increment is not in the hash_map, add it
                    if A[first_occ_idx] not in hash_map:
                        hash_map[A[first_occ_idx]] = [first_occ_idx]
                    
                    # If it is present, add the new index to its list of indexes
                    else:
                        hash_map[A[first_occ_idx]].append(first_occ_idx)

                        # Also sort that indexes out, since we need the first_occ_idx,
                        # we need it to be on the pos 0, hence sort
                        hash_map[A[first_occ_idx]].sort()

                    # Adding the current index to the element
                    hash_map[num].append(i)

                # If num exists in the dic, but not in the actual arr apart from current idx,
                # then add current idx to the hash_map
                else:
                    hash_map[num] = [i]

        # return the original list
        return A