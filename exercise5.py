#Hilario II B. Arriesgado
#EMC - Section A124

#Exercise 5 -  Equilateral Using Selection Statements
# Write a program that accepts the lengths of three sides of a triangle inputs.
# The program output should indicate whether or not the triangle is an equilateral triangle.

firstSide = int(input("Enter the first side: "))
secondSide = int(input("Enter the second side: "))
thirdSide = int(input("Enter the third side: "))

if firstSide == secondSide and thirdSide:
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")