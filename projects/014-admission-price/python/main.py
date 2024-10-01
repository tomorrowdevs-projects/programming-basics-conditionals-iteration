guest_age=input("Enter the age of the guest: ")
admission_cost=0

while guest_age!="":
    if int(guest_age)<=2:
        admission_cost+=0
        
    elif int(guest_age)>2 and int(guest_age)<13:
        admission_cost+=14.00
        
    elif int(guest_age)>64:
        admission_cost+=18.00
        
    else:
        admission_cost+=23.00
    
    guest_age=input("Enter the age of the guest: ")
    
print(f"Admission cost = {admission_cost:.2f}")