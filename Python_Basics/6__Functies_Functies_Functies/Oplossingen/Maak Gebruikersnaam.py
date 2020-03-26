def eerste_letter(naam):

    """
    >>> eerste_letter('Sansa')
    'S'
    >>> eerste_letter('Jon')
    'J'
    """
    return str(naam[0])

def gebruikersnaam(voornaam, familienaam):

    """
    >>> gebruikersnaam('Sansa', 'Stark')
    'sstark'
    >>> gebruikersnaam('Jon', 'Snow')
    'jsnow'
    """
    return str(eerste_letter(voornaam).lower() + familienaam.lower().replace(" ", ""))

#if __name__ == '__main__':
#    import doctest
#    doctest.testmod()
print("Voornaam: ")
voornaam = input()
print("Achternaam: ")
achternaam = input()
print(gebruikersnaam(voornaam, achternaam))
