
def findPairs(nums, target):
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if nums[i] == nums[j]:
				continue
			if nums[i] + nums[j] == target:
				print(i, j)

myList = [1, 2, 3, 2, 3, 4, 5]
findPairs(myList, 6)