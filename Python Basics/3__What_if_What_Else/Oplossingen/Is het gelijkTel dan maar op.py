index = 0
string1 = "Computer"
string2 = "computer"
string3 = "Computer"

if string1 == string2:
    index = index + 1
if string1 == string3:
    # index = index + 1
    index += 1
if string2 == string3:
    # index = index + 1
    index += 1

print(index)
