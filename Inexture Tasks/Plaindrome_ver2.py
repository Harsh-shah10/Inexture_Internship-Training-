n = int(input("Enter the number : "))
tmp = n
rem = 0 # for storing our reverse number
rev = 0
while(tmp>0): # end : when quotient = 0
	rem = tmp% 10 # for calculating remainder
	rev = rev * 10 + rem # fro getting reverse number
	tmp= tmp// 10 # for caclualating quotient

print("rev : ",rev)

if n==rev:
	print("Its a Palindrome Number")
elif n<0:
	print("Palindrome check is only for +ve number")
else:
	print("Its NOT a Palindrome Number")
