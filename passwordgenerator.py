import string
import random

def generator():

    s1 = string.ascii_uppercase
    # print(s1)

    s2 = string.ascii_lowercase
    # print(s2)

    s3 = string.digits
    # print(s3)

    s4 = string.punctuation
    # print(s4)

    paslength = int(input("Enter the length of password\n"))

    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)

    # the print(s) statement will generate a list consisting of both ascii uppercase and lowercase characters, digits and punctuations (special characters)
    # print(s)

    # this function will shuffle the list in the array 's' (this means they won't be arranged in the order which I have written it to print. This will shuffle s1,s2,s3,s4)
    random.shuffle(s)

    # the print(s) statement will generate a list consisting of both ascii uppercase and lowercase characters, digits and punctuations (special characters)
    # print(s)

    pas = ("".join(s[0:paslength]))
    print(pas)

generator()