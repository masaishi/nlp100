import re

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"
s_list = re.sub("[^a-zA-z]", " ", sentence).split()
two_p = [1, 5, 6, 7, 8, 9, 15, 16, 19]

d = {}
for i in range(len(s_list)):
	d[s_list[i][:(1 if i + 1 in two_p else 2)]] = i + 1
print(d)