def prime(num1 , num2):
    for i in range(num1 ,num2 + 1 ):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)


n1 = int(input('Enter lower limit of range :-'))
n2 = int(input('Enter upper limit of range :-'))
func_call = prime(n1 , n2)