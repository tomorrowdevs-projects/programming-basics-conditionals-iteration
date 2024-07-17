month=input("Enter a month:")

if month=="April" or month=="June" or month=="September" or month=="November":
    print(f"{month} = 30 days")
elif month=="February":
    print(f"{month} = 28 or 29 days") 
else:
    print(f"{month} = 31 days")