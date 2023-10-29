def isAnagram(s,t) : 
    if len(s) != len(t) :
        return False
    for x in set(s) : 
        if s.count(x) != t.count(x) : 
            return False
    return True
    

def main():
	questions = [["anagram","nagaram"], ["rat", "car"]]
	for x in questions : 
		print(isAnagram(x[0], x[1]))

if __name__ == "__main__" : 
	main()
