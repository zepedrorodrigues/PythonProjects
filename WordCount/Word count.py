words = dict()

with open(r'C:\Users\jpnms\Desktop\Cenas.txt','r') as doc:
    for line in doc:
        wrd = line.split()
        for word in wrd:
            words[word] = words.get(word,0) + 1 

wrds = words.items()
wrds1 = []

for word in wrds:
    item = (word[1],word[0])
    wrds1.append(item)

wrds_final = sorted(wrds1, reverse=True)
print(wrds_final)
