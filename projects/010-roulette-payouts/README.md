# Roulette Payouts

A roulette wheel has **38 spaces** on it.   
Of these spaces:
- 18 are red. Numbered 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34 and 36.
- 18 are black. The remaining integers between 1 and 36 are used to number the black spaces.
- 2 are green. Numbered 0 and 00   

Many different bets can be placed in roulette.  
We will only consider the following subset of them in this exercise:
- Single number (1 to 36, 0, or 00)
- Red versus Black
- Odd versus Even (Note that 0 and 00 do not pay out for even) 
- 1 to 18 versus 19 to 36

Write a program that simulates a spin of a roulette wheel **by using a random number generator**.   
Display **the number that was selected and all the bets that must be paid**. 

For example, if 13 is selected then your program should display:

```
The spin resulted in 13...
Pay 13
Pay Black
Pay Odd
Pay 1 to 18
```

If the simulation results in 0 or 00 then your program should display `Pay 0` or `Pay 00` without any further output.


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
python -m unittest python/test_roulette_payouts.py
```

or run the command from the terminal  
`python -m unittest projects/010-roulette-payouts/python/test_roulette_payouts.py`

https://spu.edu/ddowning/percal.htm

# Deadline

This project requires to be completed in a maximum of **4 hours**
