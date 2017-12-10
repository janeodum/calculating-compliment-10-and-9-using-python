"""
this my first actual python code to find the 10's and 9's compliment of numbers. still working on the 2's and 1's compliment
please leave a like.
"""

import math
import decimal

print('please \U0001f44d')

while True:
    print("options")
    print("enter 'ten' to get 10's compliment")
    print("enter 'two' to get 2's compliment")
    print("enter '1' to get 1's compliment")
    print("enter 'nine' to get 9's compliment")
    print("enter 'quit' to end the program")

    user_input=input(":")
    if user_input=="quit":
        break

    elif user_input== "ten":
        b=10
        N=float(input("enter number either float or integer"))
        a = decimal.Decimal(str(N))
        L=len(str(a).split(".")[1])
        n=len(str(a).split(".")[-2])
        Ten_comp=(math.pow(b,n) -N)
        print("the answer is " )
        print(round(Ten_comp,2))

    elif user_input== "two":
        ...
    elif user_input== "nine":
        b=10
        N = float(input("enter number either float or integer"))
        e= decimal.Decimal (str(N))
        m=e.as_tuple().exponent
        a = decimal.Decimal(str(N))
        n = len(str(a).split(".")[-2])
        f=float(math.pow(b,m))
        nine_comp=(math.pow(b,n)-f -N)
        print("the answer is " )
        print(round(nine_comp,2))
