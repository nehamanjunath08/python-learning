def greet(user):
    print(f"Hello, {user}! Welcome to day 1.")      #f"..." is an f-string (formatted string literal) which allows you to insert variables directly inside the string using {}

def ageCheck(age):
    if ( age >= 18 ):
        print("You are an adult")
    else:
        print("You are a minor")

def welcome_user(name, city):
    print(f"Hello, {name} from {city}! Welcome aboard")

def checkEvenOdd(num):
    if ( (num % 2) == 0 ):
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

def simpleCalculator():
    inputInfo = input("Enter two numbers (separated by a space):")
    num1, num2 = map(int, inputInfo.split())

    print(f"The sum of {num1} and {num2} is {num1 + num2}")

def bmiCalculator():
    inputInfo = input("Enter weight (kg) and height (cm) (separated by a space):")
    weight, height = map(int, inputInfo.split())

    bmi = weight / ((height/100) ** 2)

    if ( bmi < 18.5 ):
        category = "underweight"
    elif ( bmi >= 18.5 and bmi <= 24.9 ):
        category = "normal"
    elif ( bmi >=25 and bmi <= 29.9):
        category = "overweight"
    else:
        category = "obese"

    print(f"Your BMI is {bmi} and you are {category}")


user = input("Enter your name:")
age = int(input("Enter your age:"))
city = input("Enter your city:")
num = int(input("Enter a number:"))

greet(user)
ageCheck(age)
welcome_user(user, city)
checkEvenOdd(num)
simpleCalculator()
bmiCalculator()