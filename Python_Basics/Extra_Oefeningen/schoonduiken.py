#schoonduiken
aantalJuryleden = 0
while True:
	if aantalJuryleden < 3:
		aantalJuryleden = int(input("Geef het aantal juryleden op:"))
	else:
		score = []
		average = 0
		while aantalJuryleden > 0:
			score.append(int(input("Geef De scorce op: ")))
			aantalJuryleden-=1

		score.sort() 
		print(score)
		del score[-1]
		del score[0]
		print(score)

		avg = int(sum(score))/int(len(score))
		print(f"De gemiddelde score is {round(avg)}")
		break
