
# def remove(l, word):
#     for item in l:
#         l.remove(word)

#         return l
def remove(l, word):
    n= []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["umair", "sharjeel", "ali", "furqan"]

print(remove(l, "el"))