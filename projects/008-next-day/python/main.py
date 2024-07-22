day=int(input("Enter a day:"))
month=int(input("Enter a month:"))
year=int(input("Enter a year:"))

if year>0:
    if month==2:
        if year%400==0 or (year%4==0 and year%100!=0):
            if day>0 and day<29:
                next_day=day+1
                print(f"Input date:{year}-{month:02}-{day:02} the next day is {year}-{month:02}-{next_day:02}")
            elif day==29:
                next_day=1
                next_month=month+1
                print(f"Input date:{year}-{month:02}-{day:02} the next day is {year}-{next_month:02}-{next_day:02}")
            else:
                print("Invalid day")
        else:
            if day>0 and day<28:
                next_day=day+1
                print(f"Input date:{year}-{month:02}-{day:02} the next day is {year}-{month:02}-{next_day:02}")
            elif day==28:
                next_day=1
                next_month=month+1
                print(f"Input date:{year}-{month:02}-{day:02} the next day is {year}-{next_month:02}-{next_day:02}")
            else:
                print("Invalid day")

    elif month==4 or month==6 or month==9 or month==11:
        if day>0 and day<30:
            next_day=day+1
            print(f"Input date:{year}-{month:02}-{day:02} the next day is {year}-{month:02}-{next_day:02}")
        elif day==30:
            next_day=1
            next_month=month+1
            print(f"Input date:{year}-{month:02}-{day:02} the next day is {year}-{next_month:02}-{next_day:02}")
        else:
            print("Invalid day")

    elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
        if day>0 and day<31:
            next_day=day+1
            print(f"Input date:{year}-{month:02}-{day:02} the next day is {year}-{month:02}-{next_day:02}")
        elif day==31:
            next_day=1
            next_month=month+1
            print(f"Input date:{year}-{month:02}-{day:02} the next day is {year}-{next_month:02}-{next_day:02}")
        else:
            print("Invalid day")

    elif month==12:
        if day>0 and day<31:
            next_day=day+1
            print(f"Input date:{year}-{month:02}-{day:02} the next day is {year}-{month:02}-{next_day:02}")
        elif day==31:
            next_day=1
            next_month=1
            next_year=year+1
            print(f"Input date:{year}-{month:02}-{day:02} the next day is {next_year}-{next_month:02}-{next_day:02}")
        else:
            print("Invalid day")

    else:
        print("Invalid month")
            
else:
    print("Invalid year")