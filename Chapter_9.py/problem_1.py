f= open("poem.txt")

c= f.read()

if("twinkle" in c):
    print("Twinkle is in the Poem File")
else:
    print("Twinkle is not in the Poem File")
f.close()