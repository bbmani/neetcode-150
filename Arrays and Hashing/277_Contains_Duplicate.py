def containsDuplicate(nums):
	return len(nums) > len(set(nums))

def main():
	questions = [[1,2,3,1],[1,2,3,4],[1,1,1,3,3,4,3,2,4,2]]
	for x in questions : 
		print(containsDuplicate(x))

if __name__ == "__main__" : 
	main()
