def groupAnagrams(strs) : 
    result = {}
    
    for string in strs:
        count = [0] * 26 # a ... z
        for character in string:
            count[ord(character) - ord("a")] += 1
        
        if tuple(count) in result : 
            result[tuple(count)].append(string)
        else:
            result[tuple(count)] = [string]
    
    return list(result.values())
        

def main() :
    questions = [["eat","tea","tan","ate","nat","bat"], [""], ["a"]]
    for question in questions : 
        print(groupAnagrams(question))
    
if __name__ == "__main__" :
    main()