words = {}
word = input("Text: ")
data = word.split()
for each in data:
    if each in words:
        count = words[each]
        words[each] = count + 1
    else:
        words[each] = 1

for key in sorted(words):
    print("{} : {}".format(key,words[key]))