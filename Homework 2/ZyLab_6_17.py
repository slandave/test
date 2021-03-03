# Santiago Landaverde
# 1856681

password = input("")

new_letter = ''
i = 0
while i < len(password):
    x = password[i]
    if x == 'i':
        new_letter += '!'
    elif x == 'a':
        new_letter += '@'
    elif x == 'm':
        new_letter += 'M'
    elif x == 'B':
        new_letter += '8'
    elif x == 'o':
        new_letter += '.'
    else:
        new_letter += x
    i += 1
new_letter += "q*s"

print(new_letter)

