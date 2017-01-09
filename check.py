from pprint import pprint as pp
# Obtain input from user
try:
	print("Enter a sentence: ")
	sentence = input()	
except Exception as e:
	template = "An exception has occured."
	print(template)

# Parse input
w = sentence.split()
print(w)

# Parse words file
f = open('./words.txt', 'r').readlines()
f = map(lambda x: x.strip(), f)

hash ={}
for i in f:
	hash[i] = True


check= {}

for word in w:
	check[word] = word in hash

print("Done Checking.")
print("results: ")
pp(check)
