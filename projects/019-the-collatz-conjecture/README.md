# The Collatz Conjecture

Consider a sequence of integers that is constructed in the following manner:

Start with any positive integer as the only term in the sequence:  
    **While** the last term in the sequence is not equal to 1 **do**  
        **If** the last term is even **then**  
            Add another term to the sequence by dividing the last term by 2 using floor division  
        **Else**  
            Add another term to the sequence by multiplying the last term by 3 and adding 1

The Collatz conjecture states that this sequence will eventually end with one when it begins with any positive integer.   
Although this conjecture has never been proved, it appears to be true.     

Create a program that reads an integer, n, from the user and reports all the values in the sequence starting with n and ending with one.   
Your program should allow the user to continue entering new n values 
(and your program should continue displaying the sequences) until the user enters a value for n that is less than or equal to zero.

*The Collatz conjecture is an example of an open problem in mathematics.  
While many people have tried to prove that it is true, no one has been able to do so.    
Information on other open problems in mathematics can be found on the Internet.*


# Documentation

[Collatz Conjecture Calculator](https://goodcalculators.com/collatz-conjecture-calculator/)

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
python -m unittest python/test_the_collatz_conjecture.py
```

or run the command from the terminal  
`python -m unittest projects/019-the-collatz-conjecture/python/test_the_collatz_conjecture.py`



# Deadline

This project requires to be completed in a maximum of **2 hours**
