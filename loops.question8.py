list1 = []
for i in range(1,11):
    a = int(input(f'Enter {i} number:-'))
    list1.append(a)
print()
for n in range(0,10):

    if list1[n] > 0 :
        print(list1[n],'is a positive number')
    elif list1[n] < 0:
        print(list1[n],'is a negative number')



    if list1[n]%2==1 :
        print(list1[n],'is an odd number')
    else:
        print(list1[n],"is an even number")

    b = list1.count(list1[n])
    print('number of ', list1[n], 'in given numbers is ', b)
    print()
    print()


list2 = []
list3 = []
list4 = []
list5 = []

for i in range(len(list1)):
    if list1[i]>0:
        list2.append(list1[i])
    elif list1[i]<0:
        list3.append(list1[i])

    if list1[i]%2==1 :
        list4.append(list1[i])
    else:
        list5.append(list1[i])

print(f"The positive numbers are {list2}")
print(f"The negative numbers are {list3}")
print(f"The even numbers are {list5}")
print(f"The odd numbers are {list4}")
