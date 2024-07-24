sum=0
counter=0
while(True):
    value=float(input("Enter a value:"))
    sum=sum+value
    if sum==0 and value==0:
        print("You have entered 0 as the first value!")
        continue
    elif value==0:
        break
    counter=counter+1
    
average=sum/counter
print(f"Average = {average}")