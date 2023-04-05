import math
EarthMass=5.97600*math.pow(10,24)
G=6.6743*math.pow(10,-11)
AnotherPlanetMass=float(input("enter the mass of another planet in kg: "))
PowerOfTen=int(input("A power of 10 in the mass of another planet:"))
DistantBetweenThem=float(input("enter the distance btw Earth and another planet: "))
PowerOfTen2=int(input("A power of 10 in the distant: "))
AnotherPlanetMass=AnotherPlanetMass*math.pow(10,PowerOfTen)
DistantBetweenThem=DistantBetweenThem*math.pow(10,PowerOfTen2)
TheForceOfGravity=G*EarthMass*AnotherPlanetMass/(DistantBetweenThem**2)


print("TheForceOfGravity: ",TheForceOfGravity)