#faulty calculator

print("choose your operation")
print("1.addition\n"
      "2.subtraction\n"
      "3.multiplication\n"
      "4.division")

x=int(input())

if x==1:
    print("you chose addition,now enter the first number")
    inp1=float(input())
    print("enter the second number")
    inp2=float(input())
    print("your sum is",inp1+inp2)


elif x==2:
    print("you chose subtraction,now enter the first number")
    inp1=float(input())
    print("enter the second number")
    inp2=float(input())
    print("your differnec is",inp1-inp2)





elif x==3:
    print("you chose multiplication,now enter the first number")
    inp1=float(input())
    print("enter the second number")
    inp2=float(input())
    print("your product is",inp1*inp2)

elif x==4:
    print("you chose division,now enter the first number")
    inp1=float(input())
    print("enter the second number")
    inp2=float(input())
    print("your quotient is",inp1/inp2)

else:
    print("no operation assigned to the number you entered")