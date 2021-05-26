

#################### Q1 ####################
age = int(input("How old are you? : "))

if (age <= 18):
	print("You are very young!")
elif (age > 18 and age <= 30):
	print("You are young")
elif (age > 30 and age <= 50):
	print("You are middle-aged")
else:
	print("You are a senior citizen")
#################### Q1 ####################



#################### Q2 ####################
grade = int(input("Enter your grade: "))

if (grade >= 90):
	letter = "AA"
elif (grade >= 85 and grade < 90):
	letter = "BA"
elif (grade >= 75 and grade < 85):
	letter = "BB"
elif (grade >= 70 and grade < 75):
	letter = "CB"
elif (grade >= 65 and grade < 70):
	letter = "CC"
elif (grade >= 60 and grade < 65):
	letter = "DC"
elif (grade >= 50 and grade < 60):
	letter = "DD"
else:
	letter = "FF"
print("Your grade letter is", letter)
#################### Q2 ####################



#################### Q3 ####################
numbers = []
times = int(input("How many numbers do you want to enter? "))

for i in range(1,times+1):
	number = int(input("Enter {}. number: ".format(i)))
	numbers.append(number)

min = numbers[0]
for i in range(0,times):
	if (min > numbers[i]):
		min = numbers[i]

print("Min number you entered is", min)
#################### Q3 ####################



#################### Q4 ####################

for i in range(1,10):
	print("*" * i)

#################### Q4 ####################