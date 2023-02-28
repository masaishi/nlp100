import random

def typoglycemia(s):
	return " ".join(word[0] + "".join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1] if len(word) > 4 else word for word in s.split())

print(typoglycemia("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind"))