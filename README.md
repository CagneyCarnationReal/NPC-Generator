# NPC-Generator
## Table of Contents
-  [Features](#-features)
-  [Overview](#-overview)
-  [Code Example](#-code-example)

## Features
-  The Code has A Large Library of names to Choose from to Guarantee a new name Almost every time
-  Uses For Loops to Add information into Lists to later be used to fully print the Non Playable Characters../
-  A Single Non Playable Characters information is all in One Print Statement using "\n" to move down spaces
## Overview
The Codes Purpose is To Create ten Non Player Characters. It Starts with importing the random library, followed by making a list of over 500 names. After That the program asks The User 5 inputs for 5 Examples for jobs and Professions. After this point there is no more User input and is only computer automation. From this point there is a for loop that creates a list and adds 10 of the 500 names into a list to be used in the print statement. After this there is another For Loop that Randomly selects integers between 18 and 60 to be used as ages in a list to then be printed later. Another For Loop is used to  select one of the Five jobs and professions inputted by  the User previously and puts it into a list to be Printed later. The Next for loop finds a Float between 1 and 10,000 to be used as an Exp and is put into a List to be used Later. The Last for loop is used to find a value between the integers -100 and 100 and then puts it into a list to be used as a "Power" value to be used later.At the End there is Ten Print Statements that Print the Name,Age,Job,Exp, and Power of a Specified Non Player Character and Prints in a vertical column outlining which value is which.
## Code Example
This Code Creates a list "NPCSa" (standing for age) and picks a value between 18 and 60 11 times and puts it into that List.
```python
NPCSa = []
for i in range(11):
    NPCSa.append(random.randint(18,60))
#Create a List of ten NPCS ages
```




