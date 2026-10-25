print ("calc")
print("Welcome to the calculator")
print("1)add")
print("2)subtract")
print("3)multiply")
print("4)divide")
print("0)quit")
op=input('choose an operation:')
num1=input('enter the first number:')
num2=input('enter the second number:')
#convert string to integer for number 1
num1=int(num1)
#convert string to integer for number 2
num2=int(num2)
if op=='1':
    answer=str(num1+num2)
    num1=str(num1)
    num2=str(num2)
    print(num1+"+"+num2+"="+answer)

elif op=='2':
    answer=str(num1-num2)
    num1=str(num1)
    num2=str(num2)
    print(num1+"-"+num2+"="+answer)

elif op=='3':
    answer=str(num1*num2)
    num1=str(num1)
    num2=str(num2)
    print(num1+"*"+num2+"="+answer)

elif op=='4':
    answer=str(num1/num2)
    num1=str(num1)
    num2=str(num2)
    print(num1+"/"+num2+"="+answer)

else:
    print("that is not a choice")