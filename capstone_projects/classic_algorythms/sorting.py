"""
Sorting
Implement two types of sorting algorithms:
Merge sort and bubble sort.
"""


def merge_sort(array: list):
    # Base case
    """
    List with one or zero elements is sorted by definition.
    """
    if len(array) < 2:
        return array

    # Recursive case
    """
    Step 1. Cut array in a half.
    """
    middle_index = len(array) // 2
    left_part = array[:middle_index]
    right_part = array[middle_index:]

    """
    Step 2. Sort left part, then sort right part.
    """
    sorted_left_part = merge_sort(left_part)
    sorted_right_part = merge_sort(right_part)

    """
    Step 3. Merge sorted parts.
    """
    merged_array = []

    # While both parts are not empty compare its first elements and move the smallest one into new array
    while sorted_left_part and sorted_right_part:
        if sorted_left_part[0] > sorted_right_part[0]:
            merged_array.append(sorted_right_part.pop(0))
        else:
            merged_array.append(sorted_left_part.pop(0))

    # Then move remaining elements from one of the parts
    while sorted_left_part:  # At first, check left part
        merged_array.append(sorted_left_part.pop(0))
    while sorted_right_part:  # Then check the right part
        merged_array.append(sorted_right_part.pop(0))

    return merged_array


test_array = [38, 27, 43, 3, 9, 82, 10]
assert merge_sort(test_array) == [3, 9, 10, 27, 38,  43,  82]
