data = input("Enter a value: ")
reverse = data[::-1]

if(data == reverse ):
    print(data + " is a palindrome")
else:
    print( data + " is not a palindrome")