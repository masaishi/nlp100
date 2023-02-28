def get_n_gram(seq, n):
  return [seq[i:i + n] for i in range(len(seq) - n + 1)]

gram1 = set(get_n_gram("paraparaparadise", 2))
gram2 = set(get_n_gram("paragraph", 2))

print("Union: ", gram1 | gram2)
print("Intersection: ", gram1 & gram2)
print("Difference 1 - 2:", gram1 - gram2)
print("Difference 2 - 1:", gram2 - gram1)
print("Exist 'se' in 1?: ", 'se' in gram1)
print("Exist 'se' in 2?: ", 'se' in gram2)