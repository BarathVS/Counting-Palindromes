#Created by Oranje Maan | 2 March 2019
import math

def Validate(string):
    #Checks if string is a whole number; returns true if it is or not
    bln = False
    #Check if the number is numeric
    #One could use string.isNumeric(), but that will return false for strings such as "2.5"; the program won't accept decimals, but it will tell not to use one if one is used
    try:
        float(string)
    except:
        print("Please enter a number and only a number.")
        return bln
    #Check if the number is an integer
    if float(string).is_integer():
        #Checking if number is positive
        if float(string) < 0:
            print("Please enter a positive integer.")
        else:
            bln = True
    else:
        print("Please enter an integer.")
    return bln

def Clean(string):
    #Clean up string
    #Remove any spaces from inputed string
    string = string.replace(" ","")
    #Remove decimals points
    x = string.find(".")
    if x > -1:
        string = string[:x]
    return string

def main():
    #Get key and length; validate keys
    x = input("Give the number to serve as a palindrome's root.")
    while not Validate(x):
        x = input("Give the number to serve as a palindrome's root.")
    y = input("Give the length of the possible palindrome.")
    while not Validate(y):
        y = input("Give the length of the possible palindrome.")
    #Clean inputs
    x = Clean(x)
    y = Clean(y)
    z = math.ceil(int(y)/2) - len(x)
    a = 0
    if z >= 0:
        a = math.pow(10,z)
    print("The amount of palindromes with this root and at this length is " + Clean(str(a)) + ".")

main()
