# Santiago Landaverde
# 1856681

palindrome= input()
x = 0
y = len(palindrome)-1
result = True
while x < y:
    if palindrome[x] == ' ':
        x += 1
    elif palindrome[y] == ' ':
        y -= 1
    elif palindrome[x]!=palindrome[y]:
        result = False
        break
    else:
        x += 1
        y -= 1
if result:
    print(palindrome,"is a palindrome")
else:
    print(palindrome, "is not a palindrome")