#Hilario II B. Arriesgado
#EMC - Section A124

#Exercise 6 - Sum and Average of Numbers Using Loops and Selection Statements

#Write a program that receives a series of numbers from the user and allows
# the user to press the enter key to indicate that he or she is finished providing inputs.
#After the user presses the enter key, the program should
# print the sum of the numbers and their average

numberEntered = input('Enter a number or press Enter to quit: ')
sumOfnumberEntered = 0
count = 0

while numberEntered != "":
    number = float(numberEntered)
    sumOfnumberEntered += number
    count += 1
    avg = sumOfnumberEntered / count
    numberEntered = input('Enter a number or press Enter to quit: ')
print('The sum is ', sumOfnumberEntered)
print('The average is ', avg)

