import imp
def woordWaarde(woord):
    """
    >>> woordWaarde('Hello')
    12
    >>> woordWaarde('ComputerClub')
    36
    """
    som = int(0)

    for elkeLetter in woord:
        som += letterWaarde(elkeLetter)
    return som


def letterWaarde(letter):
    """
    >>> letterWaarde('a')
    1
    >>> letterWaarde('Q')
    10
    """
    # punten is een dictionary. Voor elke eerste "key" heeft dat een value. key "a" heeft als waarde 1 enz. Werkt als een array!
    punten = {"a": 1, "b": 3, "c": 5, "d": 2, "e": 1, "f": 4, "g": 3, "h": 4, "i": 1, "j": 4, "k": 3, "l": 3, "m": 3,
              "n": 1, "o": 1, "p": 3, "q": 10, "r": 2, "s": 2, "t": 2, "u": 4, "v": 4, "w": 5, "x": 8, "y": 8, "z": 4}
    # maak van de letter een kleine letter en geef de overeenkomstige waarde terug
    letter = letter.lower()
    return punten[letter]

# if __name__ == '__main__':
#    import doctest
#    doctest.testmod()

print("Scrabble spelen. Wat is het woord?")
woord = input()
print(f"Het woord {woord} heeft als waarde in Scrabble: {woordWaarde(woord)}.")

