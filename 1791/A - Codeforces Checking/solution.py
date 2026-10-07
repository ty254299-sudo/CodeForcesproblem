number = int(input())
word = "codeforces"
for i in range(number):
    ch = str(input())
    if ch in str(word):
        print("yes")
    else:
        print("No")