integer=int(input("Enter an integer: "))
result=""
quotient=integer

while quotient!=0:

    remainder=quotient%2
    quotient//=2
    result+=str(remainder)
    
print(f"The binary representation of {integer} is {result[::-1]}")