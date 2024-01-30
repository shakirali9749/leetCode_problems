def twosum(nums, target):
    for i in range(len(nums)): #first loop for the first element and soon
        for j in range(i + 1, len(nums)):
            if (nums[i] != nums[j]) and nums[i] + nums[j] == target:
                return [i, j]
    return "Not found"

nums = [22,21,34,4,5]
target = 9

print(twosum(nums,target))