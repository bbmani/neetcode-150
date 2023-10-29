def isAnagram(s,t) : 
    s = list(s)
    t = list(t)
    
    for x in t : 
        if x in s :
            s.pop(s.index(x))
            
    return len(s) == 0

def main():
	questions = [["anagram","nagaram"], ["rat", "car"]]
	for x in questions : 
		print(isAnagram(x[0], x[1]))

if __name__ == "__main__" : 
	main()
