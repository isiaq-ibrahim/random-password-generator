# Random Password Generator
This approach is similar to the implementation used in Google Password Manager, which suggests that users choose a strong password by mixing uppercase, lowercase, digits, and special characters. This project allows users to input the password length they wish to generate.

## How to create this project from scratch
1. Make sure you have Python installed on your machine. If you don't have it, download it from the official website https://www.python.org/
2. Download any text editor of your choice (Preferably visual Studio Code)
3. Create a new folder and open the folder in your text editor. Once you've done this, create a new Python file (passwordgenerator.py). Make sure you've set the virtual environment (you can look at my previous repository on how to do this)

Inside the passwordgenerator.py file, copy and paste this code.
```
import string
import random

def generator():

    s1 = string.ascii_uppercase
    print(s1)

    s2 = string.ascii_lowercase
    print(s2)

    s3 = string.digits
    print(s3)

    s4 = string.punctuation
    print(s4)

generator()
```

Output:
- s1 generates uppercase letters from A to Z
- s2 generates lowercase letters from a to z
- s3 generates digits from 0 - 9
- s4 generates punctuations (special characters) consisting of ~`!@#$%^&*()_-+={}[]:";',./<>?


![Screenshots](screensnaps_for_password_generator_project/s4.jpg)
