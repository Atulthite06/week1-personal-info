# Personal Information Manager

## Project Description

This is my first Python project! It's a program that stores and displays personal information.

## What I Learned

1. **Variables**: How to store different types of data
2. **Input/Output**: Getting user input and displaying results
3. **String Formatting**: Using f-strings to create nice output
4. **Error Handling**: Basic validation for user input

## How to Run This Program

1. Make sure you have Python installed.
2. Open Terminal or Command Prompt.
3. Navigate to the project folder.
4. Run:

```bash
python personal_info.py
```

5. Follow the prompts to enter your information.

## Features

* Stores static information (name, age, city, hobby)
* Gets dynamic information from the user (favorite food, favorite color)
* Displays all information in a formatted way
* Basic input validation
* Age calculation in months

## Sample Output

```text
===================================
      PERSONAL INFORMATION
===================================

Name: John Doe
Age: 25 (300 months old)
City: New York
Hobby: Reading

Favorite Food: Pizza
Favorite Color: Blue

===================================
Thank you for using the program!
===================================
```

## Challenges & Solutions

### Challenge:

User might enter empty input.

### Solution:

Added input validation using a `while` loop to ensure valid input.

### Challenge:

Formatting the output nicely.

### Solution:

Used f-strings and separators for a clean and readable display.
