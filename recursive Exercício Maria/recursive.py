def mainSubstrings(name):
    finalList = [""]
    recursive(name,finalList)
    return set(finalList)

def recursive(name,finalList):
    finalList.append(name)
    if len(name) == 1:
        return
    for i in range(len(name)):
        name = name[:i] + name[i+1:]
        recursive(name,finalList)

print(sorted(mainSubstrings("abcdef")))
