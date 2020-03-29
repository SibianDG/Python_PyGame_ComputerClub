print("Wat is je naam?")
# een "#" voor de regels zorg ervoor dat deze lijn niet uitgevoerd wordt en is dus commentaar.
# voer je naam in in de console
naam = input()
print("Naar welke podcast luister je?")
# voer de podcast in
podcast = input()

# Manier 1 om tekst te printen
print(f"Dag {naam}, jij luistert dus vaak naar {podcast}. Dat is leuk.")  # De f staat voor format. Je kan gewoon
# doorlopende tekst typen en als je een variabele erin wil steken, dan gebruik je {var}

# Manier 2:
print("Van die podcast " + podcast + " heb ik nog niet gehoord.")  # Als je + gebruikt, dan gaat Python voor en na een
# variable GEEN spaties ztten.

# Manier 3:
print('Fijn je ontmoet te hebben,', naam)  # Als je , gebruikt, dan vroegt Python zelf spaties toe. (Later zien we dat
# we dit ook nog anders kunnen aanpakken.)

