n = int(input("Enter the length of the sequence: ")) # Do not change this line

summ = 0
n1 = 0
n2 = 1
n3 = 2
print(n2)
print(n3)

for i in range(n-2):
    summ = n1 + n2 + n3
    print(summ)
    n1=n2
    n2=n3
    n3=summ