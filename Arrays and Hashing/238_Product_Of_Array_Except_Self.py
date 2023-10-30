def productExceptSelf(nums) : 
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)) : 
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1, -1, -1) : 
        res[i] *= postfix
        postfix *= nums[i]
    return res
def main() : 
    questions = [[1,2,3,4], [-1,1,0,-3,3]]
    for question in questions : 
        print(productExceptSelf(question))
        
if __name__ == "__main__" : 
    main()