# Prime Factors

The prime factorization of an integer, n, can be determined using the following steps:  

Initialize factor to 2  
**While** factor is less than or equal to n do   
    **If** n is evenly divisible by factor **then**    
        Conclude that factor is a factor of n   
        Divide n by factor using floor division   
    **Else**   
        Increase factor by 1   

Write a program that reads an integer from the user.    
If the value entered by the user is less than 2 then your program should display an appropriate error message.   
Otherwise, your program should display the prime numbers that can be multiplied together to compute n, 
with one factor appearing on each line. 

For example:

```
Enter an integer (2 or greater): 72 The prime factors of 72 are:
2
2
2 
3 
3
```

# Documentation

For this project solution you may use:

- Variables, expressions, statements
- Conditionals and recursion
- Iteration
- Strings


# Test
Execute the test to validate your solution.  

**VSCODE**   
To run the test command from the README.md install the extension **runme**. 
Press Ctrl+Shift+x search and install the **runme** extension. 


**Python**

```sh
python -m unittest python/test_prime_factors.py
```

or run the command from the terminal  
`python -m unittest projects/020-prime-factors/python/test_prime_factors.py`



# Deadline

This project requires to be completed in a maximum of **2 hours**
