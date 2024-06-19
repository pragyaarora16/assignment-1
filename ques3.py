
def fact(num):
    if (num==0) or (num==1):
     return 1
    elif (num<0):
        print("Invalid input")
    else :
     return num* fact(num-1)

num=int(input("enter a number"))
result=fact(num)
print(result)