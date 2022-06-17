# input_string == input_string_reverse : means it's palindrome

input_string = input(str("Enter a string : "))
reverse = input_string[::-1]
if input_string == reverse:
    print("Its a Palindrome String Dude")
else:
    print("Its NOT a Palindrome String Dude")
