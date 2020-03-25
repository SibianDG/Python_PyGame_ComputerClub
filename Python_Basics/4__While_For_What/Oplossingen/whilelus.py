index = 0
herhalen = True
while herhalen:
    if index > 4:
        print("herhalen op false zetten -> while stoppen")
        herhalen = False
    index += 1
print("De index", index)