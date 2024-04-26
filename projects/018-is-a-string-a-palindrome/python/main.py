string=input("Please, enter the string you are interested in:")

if len(string)%2==0:
    index=0
    while index<len(string)/2:
        char1=string[index]
        char2=string[len(string)-index-1]
        if char1==char2:
            index+=1
        else:
            print('{} is not a palindrome'.format(string))
            break
    if index==len(string)/2:
        print('{} is a palindrome'.format(string))
else:
    index=0
    while index<(len(string)-1)/2:
        char1=string[index]
        char2=string[len(string)-index-1]
        if char1==char2:
            index+=1
        else:
            print('{} is not a palindrome'.format(string))
            break
    if index==(len(string)-1)/2:
        print('{} is a palindrome'.format(string))