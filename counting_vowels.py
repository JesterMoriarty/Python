# Count the numbre of vowels in each word in a string 
# and print the number of vowels in each word in a string


sentence = "The quick brown fox jumped over the lazy dog"
x = sentence.split()

v = 0
for word in x:
    for letter in word:
        if letter in "aeiouAEIOU":
            v += 1
    print(word, "has", v, "vowels")
    v = 0

# -----------------------------------------------------------
sentence = "The quick brown fox jumped over the lazy dog"

vovels = "aeiou"

x = sentence.split()

print(x)

v = []

for i in x:
    c = 0
    for j in i:
        if j in vovels:
            c += 1
    v.append(str(c))
    print(v)
print(" ".join(v))

# -----------------------------------------------------------