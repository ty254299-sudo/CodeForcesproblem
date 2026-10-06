s = input().strip()
 
x = len(set(s))
if x % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")