# mosalas bodan
x=int(input("a num"))
y=int(input("a num"))
z=int(input("a num"))
while True:
    if x<=0:
        x=int(input("a num"))
        continue
    if y<=0:
        y=int(input("a num"))
        continue
    if z<=0:
        z=int(input("a num"))
        continue
    break
if x+y>z:
    if x+z>y:
        if y+z>x:
            print ("is Triangle")
        else:
            print ("is not Triangle")
    else:
        print ("is not Triangle")
else:
     print("is not Triangle")
