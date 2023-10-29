def twoSums(nums, target) : 
    prevMap = {} # Value, Index
    
    for index, value in enumerate(nums) : 
        diff = target - value
        if diff in prevMap:
            return [prevMap[diff], index]
        prevMap[value] = index
    
    return

def main() : 
    questions = [[[2,7,11,15], 9], [[3,2,4], 6], [[3,3], 6]]
    for question in questions : 
        print(twoSums(question[0], question[1]))
        
if __name__ == "__main__" : 
    main()