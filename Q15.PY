a = int(input("enter the number"))
b = int(input("enter the number"))
c = int(input("enter the number"))
if(a+b>c) and (a+c>b) and (b+c>a):
    print("Triangle is valid")
else:
    print("Triangle is not valid")