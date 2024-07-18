column=input("Enter the letter of the column:")
row=int(input("Enter the number of the row:"))

if column=="a" or column=="c" or column=="e" or column=="g":
    if (row%2)!=0:
        square="black"
    else:
        square="white"    
elif column=="b" or column=="d" or column=="f" or column=="h":
    if (row%2)!=0:
        square="white"
    else:
        square="black"    
        
print(f"{column}{row} = {square}")    