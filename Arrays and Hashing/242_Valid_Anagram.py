def isAnagram(s,t) : 
    s = sorted(list(s))
    t = sorted(list(t))
    
    return s == t
    
    

def main():
	questions = [["anagram","nagaram"], ["rat", "car"]]
	for x in questions : 
		print(isAnagram(x[0], x[1]))

if __name__ == "__main__" : 
	main()
