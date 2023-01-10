# Python program for the above approach
from collections import Counter

# Function to remove common
# words from two strings
def removeCommonWords(sent1, sent2):
	
	# Store the words present
	# in both the sentences
	sentence1 = list(sent1.split())
	sentence2 = list(sent2.split())
	
	# Calculate frequency of words
	# using Counter() function
	frequency1 = Counter(sentence1)
	frequency2 = Counter(sentence2)


	word = 0
	
	# Iterate the list consisting
	# of words in the first sentence
	for i in range(len(sentence1)):
		
		# If word is present
		# in both the strings
		if sentence1[word] in frequency2.keys():
			
			# Remove the word
			sentence1.pop(word)
			
			# Decrease the frequency of the word
			word = word-1
		word += 1
		
	word = 0
	
	# Iterate the list consisting of
	# words in the second sentence
	for i in range(len(sentence2)):
		
		# If word is present
		# in both the strings
		if sentence2[word] in frequency1.keys():
			
			# Remove the word
			sentence2.pop(word)
			
			# Decrease the removed word
			word = word-1
			
		word += 1
		
	# Print the remaining
	# words in the two sentences
	print(*sentence1)
	print(*sentence2)


# Driver Code

sentence1 = "sky is blue in color"
sentence2 = "raj likes sky blue color"

removeCommonWords(sentence1, sentence2)
