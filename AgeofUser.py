from datetime import datetime

user=input("Enter Your Birth YYYY-MM-DD: ")
birth_date = datetime.strptime(user, "%Y-%m-%d")

current_date = datetime.now()
age = current_date.year - birth_date.year

if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"You are {age} years old.")
