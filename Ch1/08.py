def chipher(s):
	return ''.join([chr(219 - ord(c)) if c.islower() else c for c in s])

sentence = "I am an NLPer"
print("Original sentence: ", sentence)

sentence = chipher(sentence)
print("Chipher sentence: ", sentence)

sentence = chipher(sentence)
print("Decipher sentence: ", sentence)