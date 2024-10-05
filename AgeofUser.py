current_year=2024
print("Current year:",current_year)
user=int(input("Enter Your Birth Year: "))

if user>current_year:
    print("Your Birth year input is more than current year")
else:
    age=current_year-user
    print("Your Age:", age)    