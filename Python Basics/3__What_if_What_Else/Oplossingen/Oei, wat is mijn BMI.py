#input
gewicht = int(input())
# lengte in cm ingeven
lengte = int(input())

#bmi berekenen
bmi = (gewicht)/(lengte/100)**2
interpretatie = ''

#berekenen
if bmi < 18:
    interpretatie = 'ondergewicht.'
elif 18 < bmi < 25:
    interpretatie = 'normaal gewicht.'
elif 25 < bmi < 27:
    interpretatie = 'licht overgewicht.'
elif 27 < bmi < 30:
    interpretatie = 'matig overgewicht.'
elif 30 < bmi < 40:
    interpretatie = 'ernstig overgewicht.'
else:
    interpretatie =  'ziekelijk overgewicht.'

#print
print('Een persoon van', gewicht, 'kg met een lengte van', lengte, 'cm heeft', interpretatie)

