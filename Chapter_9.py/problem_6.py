
with open("log.txt", "r") as f:
    c= f.read()

if ("python" in c):
    print("Python is in the content log")