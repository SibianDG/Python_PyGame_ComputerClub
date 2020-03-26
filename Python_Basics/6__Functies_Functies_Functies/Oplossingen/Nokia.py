def vraagWoord():
    print("Welk woord wil je typen op een Nokia?")
    return str(input())


def nokiaTypen(woord):
    resultaat = ""
    for letter in woord:
        resultaat += str(toetsen(letter) + " ")
    return resultaat


def toetsen(letter):
    toetsIngedrukt = ""
    toetsenArray = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    letter = letter.lower()

    for toetsIndex in range(len(toetsenArray)):
        if letter in toetsenArray[toetsIndex]:

            plaatsOpToets = toetsenArray[toetsIndex].index(letter)
            for _ in range(plaatsOpToets+1):
                toetsIngedrukt += str(toetsIndex)

    return toetsIngedrukt


# if __name__ == '__main__':
#    import doctest
#    doctest.testmod()
print(nokiaTypen(vraagWoord()))

