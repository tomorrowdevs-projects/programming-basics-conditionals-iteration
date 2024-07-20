year=int(input("Enter a year:"))

if year%400==0:
    print(f"{year} = Leap year")

elif year%4==0 and year%100!=0:
    print(f"{year} = Leap year")
    
else:
    print(f"{year} = Not leap year")