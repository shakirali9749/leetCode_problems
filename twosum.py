def twosum(nums,target):
	for i in range(len(nums)):
		for j in range(i+1,len(nums)):
			if target-nums[i] == nums[j]:
				# 26-11 == 14 
				# 26-11 == 15(15 == 15)
				return[i,j]
	return None


test = [2,7,11,14,15]
target = 26
print(twosum(test,target))	

# index starts from zero
# length starts from one