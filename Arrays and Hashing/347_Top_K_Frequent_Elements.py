def topKFrequent(nums, k) : 
    result = {} # value, count
    for x in nums : 
        if x in result : 
            result[x] += 1
        else : 
            result[x] = 1
    
    result = dict(sorted(result.items(), key=lambda x:x[1], reverse=True))
    return list(result.keys())[:k]

def main() : 
    questions = [[[1,1,1,2,2,3], 2], [[1], 1]]
    for question in questions : 
        print(topKFrequent(question[0], question[1]))
        
if __name__ == "__main__" : 
    main()