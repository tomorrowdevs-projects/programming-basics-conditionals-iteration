# Decimal to Binary

Write a program that converts a decimal (base 10) number to binary (base 2).   

Read the decimal number from the user as an integer and then 
use the division algorithm shown below to perform the conversion. 

When the algorithm completes, result contains the binary representation of the number.   
Display the result, along with an appropriate message.

Let *result* be an empty string   
Let *q* represent the number to convert    
**repeat**   
    Set *r* equal to the remainder when *q* is divided by 2   
    Convert *r* to a string and add it to the beginning of result   
    Divide *q* by 2, discarding any remainder, and store the result back into *q*   
**until** *q* is 0   


# Documentation

[Decimal/Binary Conversion Table](https://www.exploringbinary.com/decimal-binary-conversion-table/)

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
python -m unittest python/test_decimal_to_binary.py
```

or run the command from the terminal  
`python -m unittest projects/021-decimal-to-binary/python/test_decimal_to_binary.py`



# Deadline

This project requires to be completed in a maximum of **2 hours**
