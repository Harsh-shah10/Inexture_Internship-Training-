while True:
    n = input("Enter the height of Diamond : ")
    if n.isnumeric()==True:
        n = int(n)
        break
    else:
        print('Sorry ! Only integers Accepted')

# Upward pyramid
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end=' ')
    for k in range(2 * i + 1):
        print('* ', end='')
    print()

# Lower pyramid
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end=' ')
    for k in range(2*(n - i - 1) - 1):
        print('* ', end='')
    print()