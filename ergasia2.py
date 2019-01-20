check="false"
while check not in ("true"):
    num = int(input("δώστε εναν αριθμο μεχρι το 1000000: "))
    if num>=1 and num<=1000000:
       check="true"
piliko=num
ginomeno=1
i=1
while ginomeno<num :

    i+=1
    dinami=0
    while piliko%i==0:
        piliko=piliko//i
        dinami=dinami+1

    if dinami>1 :
        ginomeno=ginomeno*(i**dinami)
        print ("(",i,"**",dinami,")",end = " ")
    elif dinami==1 :
        ginomeno=ginomeno*i
        print ("(",i,")",end = " ")
