
def question_1():
    n = 4
    for i in range(0, n):
        print(" " * (n - i), end="")
        for j in range(0, i+1):
            print("*",end="")
        print()

    print("*" * ((n * 2) + 1))

    for i in range(n, 0, -1):
        print(" " * n, end="")
        for j in range(1, i + 1):
            print("*", end='')
        print()
#question_1()

#################################################
def question_2():
    currencies = [400, 1000, 500, 1500, 800]
    usd = 8.20
    eur = 9.90

    print("Currency Converter ")
    print("1. USD to TRY")
    print("2. TRY to USD")
    print("3. EUR to TRY")
    print("4. TRY to EUR")
    choise = int(input("Enter your selection (1-4)  to convert the values [400, 1000, 500, 1500, 800]: "))

    converted = []
    if (choise == 1):
        for currency in currencies:
            converted.append(currency * usd)
    elif (choise == 2):
        for currency in currencies:
            converted.append(currency / usd)
    elif (choise == 3):
        for currency in currencies:
            converted.append(currency * eur)
    elif (choise == 4):
        for currency in currencies:
            converted.append(currency / usd)
    print("TRY/USD/EUR equivalents are: ", converted)
#question_2()

#################################################

def calculate_avarage():
    sum = 0
    count = 0
    while True:
        number = int(input("Enter number (to Exit Enter Negative Number): "))
        if (number > 0):
            sum = sum + number
            count = count + 1
        else:
            break
    return sum / count
#print("The avarege number is", calculate_avarage())

#################################################

def factoriel(n):
    if n == 1:
        print(n,"! =",n)
        return 1
    else:
        print(n,"! = ",n,"*",n - 1,"!")
        return n * factoriel(n - 1)
#n = int(input("Enter a number less than 10 (exlusive): "))
#print("The factorial of n is", factoriel(n))

#################################################

def towers_of_hanoi(n, source, destination, auxilarity):
    if (n == 1):
        print("Moving disk 1 from stick", source, "to stick", destination)
        return
    else:
        towers_of_hanoi(n-1, source, auxilarity, destination)
        print("Moving disk", n, "from stick", source, "to stick", destination)
        towers_of_hanoi(n-1, auxilarity, destination, source)
towers_of_hanoi(3, "C", "B", "A")