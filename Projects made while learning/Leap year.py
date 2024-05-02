year = int(input("Enter the year : "))
if year%4 == 0:
    print(f"The year {year} is divisible by 4(Leap)")
    if year%100 != 0:
        print(f"The year {year} is divisible by 100(leap)")
    else:
        print(f"The year {year} is not divisible by 200(Not leap)")
        if year%400 == 0:
            print(f"The year {year} is Divisible by 400(leap).\nSo the year is a leap year")
        else:
            print(f"The year {year} is not Divisible by 400(Not leap)\nSo the year is not a leap year")
else:
    print(f"The year {year} is not a leap year")

