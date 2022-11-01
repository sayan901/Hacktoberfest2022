terms = 10
fibonacci_list=[]
n1, n2 = 0, 1
count = 0

if terms <= 0:
    pass
elif terms == 1:
   fibonacci_list.append(n1)
else:
   while count < terms:
       fibonacci_list.append(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
  
primenumbers=[]

for number in range (0, 24 + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            primenumbers.append(number)


def printNumber(list, index):
    print(str(list[index]) + " ", end="")

for i in range(len(primenumbers)+1):
    printNumber(fibonacci_list, i)
    if len(primenumbers)!=i:
        printNumber(primenumbers, i)