day=int(input("Enter your day of birth:"))
month=input("Enter your month of birth:")

if month=="December":
    if day>=1 and day<=21:
        print(f"{day} {month} = Sagittarius")
    elif day>21 and day<=31:
        print(f"{day} {month} = Capricorn")  

elif month=="January":
    if day>=1 and day<=19:
        print(f"{day} {month} = Capricorn")
    elif day>19 and day<=31:
        print(f"{day} {month} = Aquarius")

elif month=="February":
    if day>=1 and day<=18:
        print(f"{day} {month} = Aquarius")
    elif day>18 and (day<=28 or day<=29):
        print(f"{day} {month} = Pisces")

elif month=="March":
    if day>=1 and day<=20:
        print(f"{day} {month} = Pisces")
    elif day>20 and day<=31:
        print(f"{day} {month} = Aries")

elif month=="April":
    if day>=1 and day<=19:
        print(f"{day} {month} = Aries")
    elif day>19 and day<=30:
        print(f"{day} {month} = Taurus")    

elif month=="May":
    if day>=1 and day<=20:
        print(f"{day} {month} = Taurus")
    elif day>20 and day<=31:
        print(f"{day} {month} = Gemini")

elif month=="June":
    if day>=1 and day<=20:
        print(f"{day} {month} = Gemini")
    elif day>20 and day<=30:
        print(f"{day} {month} = Cancer")

elif month=="July":
    if day>=1 and day<=22:
        print(f"{day} {month} = Cancer")
    elif day>22 and day<=31:
        print(f"{day} {month} = Leo")

elif month=="August":
    if day>=1 and day<=22:
        print(f"{day} {month} = Leo")
    elif day>22 and day<=31:
        print(f"{day} {month} = Virgo")

elif month=="September":
    if day>=1 and day<=22:
        print(f"{day} {month} = Virgo")
    elif day>22 and day<=30:
        print(f"{day} {month} = Libra")

elif month=="October":
    if day>=1 and day<=22:
        print(f"{day} {month} = Libra")
    elif day>22 and day<=31:
        print(f"{day} {month} = Scorpio")

elif month=="November":
    if day>=1 and day<=21:
        print(f"{day} {month} = Scorpio")
    elif day>21 and day<=30:
        print(f"{day} {month} = Sagittarius")

else:
    print("You have entered a wrong day or month!")