


#################### Q1 ####################
sum = 0
count = 0
while True:
    number = int(input("Enter the negative number: "))
    if (number < 0):
        sum = sum + number
        count = count + 1
    else:
        break
print("The avarege number is", sum / count)
#################### Q1 ####################



#################### Q2 ####################
while True:
    text = input("Enter a string(to Exit press enter): ")
    if (text == ""):
        break
    print(text)
print("You are done!")
#################### Q2 ####################



#################### Q3 ####################
i = 2
while i < 51:
    j = 2
    isItPrime = True
    while j < i:
        if (i % j == 0):
            isItPrime = False
            break
        j = j + 1
    if isItPrime:
        print(j)
    i = i + 1
#################### Q4 ####################