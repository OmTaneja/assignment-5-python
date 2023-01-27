a = 65
x = int(input("Enter range :  "))
for i in range(x):
    for j in range(i+1):
        b = chr(a)
        print(b,end='')
        a+=1
    print()