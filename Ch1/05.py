def get_n_gram(seq, n):
  return [seq[i:i + n] for i in range(len(seq) - n + 1)]

t = "I am an NLPer"
print("Word bi-grams: ", get_n_gram(t.split(), 2))
print("Letter bi-grams: ", get_n_gram(t, 2))