for index in range(ord('a'), ord('z')+1):
    print(index, end= ' ')


dic = { "a" : 1, "b": 3, "z" : 12}
if "z" in dic:
    print("in dict")
    print(dic["z"])


groot = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
klein = "abcdefghijklmnopqrstuvwxyz"

string = "{"
#for letter in groot:
#    string += "pygame.K_" + letter + " : \"" + letter + "\", "
for letter in klein:
    string += "pygame.K_" + letter + " : \"" + letter + "\", "
string += "}"
print(string)
