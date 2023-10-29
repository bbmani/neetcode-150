def isAnagram(s, t):
	return list(set(s)) == list(set(t))

def main():
	questions = [["anagram","nagaram"], ["rat", "car"]]
	for x in questions : 
		print(isAnagram(questions[0], questions[1]))

if __name__ == "__main__" : 
	main()
