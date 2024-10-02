string=input("Enter a string: ")
i=0
j=len(string)-1

while i<j:
    if string.lower()[i]!=string.lower()[j]:
        result="is not a palindrome"
    else:
        result="is a palindrome"
    i+=1
    j-=1

print(f"{string} {result}")