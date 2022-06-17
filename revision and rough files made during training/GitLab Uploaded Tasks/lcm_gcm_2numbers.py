# Finding prime factors of a number
def prime_factors(n,lst):
    tmp = n
    i = 2 #least_prime_no 2
    while tmp>1:
        if tmp%i==0:
            lst.append(i)
            tmp/=i
        else:
            i+=1

# for validation of taking numbers as inputs are Integers
while True:
    num1 = input("Enter 1st number : ")
    num2 = input("Enter 2nd number : ")
    if num1.isnumeric()==True and num2.isnumeric()==True:
        num1 = int(num1)
        num2 = int(num2)
        break
    else:
        print('Sorry ! Only integers Accepted')

# for fetching prime factors for the number
l1 = []
l2 = []
prime_factors(num1,l1)
prime_factors(num2,l2)

print(f"Prime factors of {num1} : ",l1)
print(f"Prime factors of {num2} : ",l2)
# Python code to count the number of occurrences
def count_no(lst, no):
    count = 0
    for i in lst:
        if i == no:
            count = count + 1
    return count

# getting the unique number in both the list in set_lst
set_lst = list(set(l1+l2))

# dict consisting of count records
dic_count = {}

for i in set_lst:
    tmp = []
    a = count_no(l1, i)
    b = count_no(l2, i)
    tmp.append(a)
    tmp.append(b)
    dic_count[i]=tmp
#print("dic : ",dic_count)

# for finding lcm for 2 numbers
lcm = 1
for i in dic_count:
    a = i**(max(dic_count[i]))
    #print("value generated for lcm : ",a)
    lcm*=a

print(f"The LCM of {num1} and {num2} is ",lcm)

# for HCD/GCM 
def gcm(n1, n2):
   while(n2):
       n1, n2 = n2, n1 % n2
   return n1

print(f"The GCM of {num1} and {num2} is ",gcm(num1,num2))
