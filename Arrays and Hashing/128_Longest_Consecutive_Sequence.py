def longestConsecutive(nums) : 
    longest = 0
    numSet = set(nums)
    
    for n in nums : 
        if (n-1) not in numSet:
            length = 0
            while (n+length) in numSet:
                length += 1
            longest = max(length, longest)
    
    return longest

def main() : 
    questions = [[100,4,200,1,3,2], [0,3,7,2,5,8,4,6,0,1]]
    for question in questions : 
        print(longestConsecutive(question))
    
if __name__ == "__main__" :
    main()