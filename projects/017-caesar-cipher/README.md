# Caesar Cipher

One of the first known examples of encryption was used by Julius Caesar.   
Caesar needed to provide written instructions to his generals, 
but he didn’t want his enemies to learn his plans if the message slipped into their hands.   
As a result, he developed what later became known as the Caesar cipher.  

The idea behind this cipher is simple (and as such, it provides no protection against modern code breaking techniques).   
Each letter in the original message is shifted by 3 places.   
As a result, A becomes D, B becomes E, C becomes F, D becomes G, etc.

The last three letters in the alphabet are wrapped around to the beginning:    
X becomes A, Y becomes B and Z becomes C. 

Non-letter characters are not modified by the cipher.

Write a program that implements a Caesar cipher.   
Allow the user to supply the message and the shift amount, and then display the shifted message.  

Ensure that your program encodes both uppercase and lowercase letters.  
Your program should also support negative shift values so that it can be used both to encode messages and decode messages.

# Documentation
[Caesar Cipher Online](https://cryptii.com/pipes/caesar-cipher)


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
python -m unittest python/test_caesar_cipher.py
```

or run the command from the terminal  
`python -m unittest projects/017-caesar-cipher/python/test_caesar_cipher.py`



# Deadline

This project requires to be completed in a maximum of **2 hours**
