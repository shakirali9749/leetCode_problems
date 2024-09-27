"""
remove zeroz from end othe the list 1
and after that add list 2 in list1
"""


def remove_trailing_zeroz(list1,list2):
    while list1[-1] == 0:
        list1.pop()
    list1 = list1 + list2
    list1.sort()
    return list1

# simple lists for test
num1 = [1,2,3,0,0,0,0] 
num2 = [1,2,3,]
print(remove_trailing_zeroz(num1,num2))