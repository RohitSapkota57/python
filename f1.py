
def add():
    sum=a+b
    print("addition is ",sum)

a=int(input("enter first number : "))
b=int(input("enter second number : "))
add()

def hello(name):
    print(name,"\n\this is hello to you "  +"\ni hope you are doing well \n")
    return"well done"

hello("harish")
a=hello("hari")
print(a)


def rupee(n):   ##currency conveter
    rs=n*140.45
    print(f"{n}$ is {rs} in nepali currency ")
a=int(input("\nEnter dollor($) : "))
rupee(a)

def sum(n):                      ##factroial
    if (n==1):
        return 1
    return sum(n-1)+n
a=int(input("\nenter number : "))

print(sum(a))


