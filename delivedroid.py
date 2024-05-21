p = int(input(""))
c = int(input(""))

points = 50*p - 10*c

if p > c:
    points += 500

print(points)