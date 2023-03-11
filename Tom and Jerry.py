x=int(input("Jerry's speed: "))
y=int(input("Tom's speed: "))
if (x>y) or (y<=0):
    print ("Tom won't catch up with Jerry")
else:
    s=int(input("The initial distance between them: "))
    a=s*x//(y-x)
    t=a//x
    print("Tom will catch up with Jerry in " , t , 'seconds')