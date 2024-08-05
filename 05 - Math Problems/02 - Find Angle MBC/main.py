import math

AB = int(input().strip())
BC = int(input().strip())

AC = math.sqrt(AB**2 + BC**2)
BM = AC / 2
angle = math.acos(BC / (2 * BM))
angle = math.degrees(angle)
print(round(angle), chr(176), sep='')
