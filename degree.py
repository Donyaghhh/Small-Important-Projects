while True :
    grade=float(input("enter a score"))
    if grade >= 18 and grade <=20:
        print ("A")
        continue
    if grade >=14 and grade <=17:
        print ("B")
        continue
    if grade >=10 and grade <=13:
        print ("C")
        continue
    if grade < 9:
        print ("D")
        continue
    if grade <= 0 or grade >=20:
        print ("Invalid")
