a1 = int(input('enter lower limit of range: '))
a2 = int(input('enter upper limit of range: '))
b = int(input('enter number for which divisibility is to be checked : '))

for i in range(a1,a2):
    if i%b==0:
        print(i)