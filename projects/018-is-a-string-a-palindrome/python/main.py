string_origin=input("Enter a string: ")
string=string_origin.lower()
i=1
half_lenght=len(string)//2

is_palindrome=True
while is_palindrome and i<=half_lenght:
    if string[i-1]!=string[-i]:
        is_palindrome=False
    i+=1

if is_palindrome:
    print(f"{string_origin} is a palindrome")
else:
    print(f"{string_origin} is not a palindrome")