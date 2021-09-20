angle1=int(input("enter the number"))
angle2=int(input("enter the number"))
angle3=int(input("enter the number"))
sum = angle1+angle2+angle3
if (sum==180 and angle1 >= 0 and angle2 >= 0 and angle3 >= 0):
    print("triangle is valid")
else:
    print("triangle is not valid")