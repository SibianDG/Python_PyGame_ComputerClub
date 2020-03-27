array = ["x", "o", "x"] # is 1 rij.
array2 = [["x", "o", "x"], ["x", "x", "x"], ["x", "o", "x"]] #is een 2 dimensionale array.
# ik wil teken in het midden. rijen 0 - 1 - 2 => 1; kolommen 0 - 1 - 2 => 1
print(array2[1][1]) # dat element uitprinten.
print()
# spelbord uitprinten:
for rij in array2:
    # rij is een array: ["x", "o", "x"]
    for kolom in rij:
        print(kolom, end=' ')
    print() #print new line
