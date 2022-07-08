from cmath import sqrt
from math import floor


option = 'y'
print("Enter square/cube side length\n")
sides = int(input())

#main
while(option != 'q'):

    print("Enter current coordinates (if no z, enter 0)")
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))

    print("Enter coordinates of the space you wish to go to (if no z, enter 0)")
    xm = int(input("x: "))
    ym = int(input("y: "))
    zm = int(input("z: "))

    print("Calculating...")

    #Calculate the differences between destination and origin
    xd = abs(xm - x)
    yd = abs(ym - y)
    zd = abs(zm - z)

    #Using triangle side lengths, peform pyth to get distance
    c = ((xd**2) + (yd**2) + (zd**2))**0.5

    #Round c to nearest multiple of side length
    roundedc = floor(c + .5)
    cd = c * sides
    cdrounded = roundedc * sides

    print("Float distance is: " + str(c))
    print("Rounded distance is: " + str(roundedc))
    print("Distance from origin to destination (in your units): " + str(cd))
    print("Distance from origin to destination rounded to whole side lengths (in your units): " + str(cdrounded))

    print("If you wish to run another calculation, hit enter. If not, hit q then enter.")
    option = input()
    print(option)