
celcius_value = [100, 0, 30, 10] 
fahrenheit_value = [212, 32, 86, 50] 

def celcius_to_fahrenheit(celcius):
    print("The Fahreneit equivalents are ", end= '')
    for i in range(4):
        fahreneit  = (celcius[i] * 1.8) + 32
        print(fahreneit, end=' ')
    print()

def fahreneit_to_celcius(fahrenheit):
    print("The Celcius equivalents are ", end= '')
    for i in range(4):
        celcius = (fahrenheit[i] - 32) / 1.8
        print(celcius, end=' ')
    print()

print("Temperature Conversion Program")
print("1.	Convert from Celcius to Fahrenheit")
print("2.	Convert from Fahrenheit to Celcius")
choice = int(input("Choice (1/2):"))

if (choice == 1):
    celcius_to_fahrenheit(celcius_value)
else:
    fahreneit_to_celcius(fahrenheit_value)

print("")