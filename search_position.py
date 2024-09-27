"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

"""

# steps 1: find the index of target if available in list
# step2: if target not available in list then add target in list , and return the target index

def search_position(num_list, target):
    if target in num_list:
    	return num_list.index(target)
    else:
    	num_list.append(target)
    	num_list.sort()
    	return num_list.index(target)
    	


# Test with example cases
num_list = [1, 3, 5, 6]
target = 9
print(search_position(num_list, target))  # Output: 2

# num_list = [1, 3, 5, 6]
# target = 2
# print(search_position(num_list, target))  # Output: 1

# num_list = [1, 3, 5, 6]
# target = 7
# print(search_position(num_list, target))  # Output: 4





