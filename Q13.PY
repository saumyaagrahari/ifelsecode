amount=int(input("enter the amount"))
note=int(input("enter the note"))
if (amount>=5000):
    print("amount/5000),(note 5000*5000")
elif (amount>=100):
    print("amount/100),(note 100*100")
elif (amount>=50):
    print("amount/50),(note 50*50")
elif (amount>=20):
    print("amount/20),(note 20*20")
elif (amount>=10):
    print("amount/10),(note 10*10")
elif (amount>=5):
    print("amount/5),(note 5*5")
elif (amount>=2):
    print("amount/2),(note 2*2")
elif (amount>=1):
    print("amount/1),(note 1*1")
else:
    print("amount is not match")

