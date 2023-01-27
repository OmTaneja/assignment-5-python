a = int(input('enter length of 1st side:-'))
b = int(input('enter length of 2nd side:-'))
c = int(input('enter length of 3rd side:-'))


if a<=b+c and b<=a+c and c<=b+c :
    s = (a+b+c)/2
    area =((s)*(s-a)*(s-b)*(s-c))**(0.5)
    print(area)