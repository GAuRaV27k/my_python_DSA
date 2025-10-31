"""
    Given a list of integers, return elements a, b, c such that a + b + c = 0.
    Args:
        nums: list of integers
    Returns:
        list of lists of integers where sum(each_list) == 0
    Examples:
        >>> find_triplets_with_0_sum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
        >>> find_triplets_with_0_sum([])
        []
        >>> find_triplets_with_0_sum([0, 0, 0])
        [[0, 0, 0]]
        >>> find_triplets_with_0_sum([1, 2, 3, 0, -1, -2, -3])
        [[-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
"""   
# we find the sum using the hashing 
def find_triplets_with_0_sum_hashing(arr):
        target_sum = 0 
        output_array = []

        for index , item in enumerate(arr[:-2]):
                
                # to store second elements that can complement the final sum.
                set_init = set()
                # current sum needed for reaching the target sum
                current_sum = target_sum - item                
                # Traverse the subarray arr[i+1:].
                for second in arr[index+1:]:
                        # required sum of second element 
                        required_value = current_sum - second


                        # Verify if the desired value exists in the set.
                        if required_value in set_init:
                                # find the triplet 
                                combination_value = sorted([item, second, required_value])
                                if combination_value not in output_array:
                                    output_array.append(combination_value)
                        # Include the current element in the set
                        # for subsequent complement verification.
                        set_init.add(second)
        print(output_array)

find_triplets_with_0_sum_hashing([-1, 0, 1, 2, -1, -4])




