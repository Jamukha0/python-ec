# aSSIGNMENT DAY4 

# PALINDROME CHECK CASE SENSITIVE

a=input("enter the string")
if a == a[::-1]:
    print("palindrome")
else:
    print("not palindrome")
    
# # PALINDROME CHECK NON CASE SENSITIVE
# can use .upper() or .lower()

a=input("enter the string").upper()    
if a == a[::-1]:
    print("palindrome")
else:
    print("not palindrome")