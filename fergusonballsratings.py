n = int(input(""))
starrating = []
for i in range(0, n):
    points = int(input(""))
    fouls = int(input(""))
    
    stars = points*5-fouls*3
    starrating.append(stars)

starplayers = 0
for playerstars in starrating:
    if playerstars > 40:
        starplayers += 1
plus = ""
if starplayers == n:
    plus = "+"
output = str(starplayers) + plus
print(output)