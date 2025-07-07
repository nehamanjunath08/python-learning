def greet(user):
    print(f"Hello, {user}! Welcome to day 1.")      #f"..." is an f-string (formatted string literal) which allows you to insert variables directly inside the string using {}

user = input("Enter your name:")
greet(user)