string=input("Enter the value of PALINDROME:")
rev_string = string[::-1]
print("The Reverse String :",rev_string)

if string == rev_string:
    print("IT is palindrome")
else:
    print("Not a palindrome")
