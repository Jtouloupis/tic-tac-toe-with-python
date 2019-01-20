diast1="0"
list_f=[]
while diast1!="" :   
 diast1 = input("πληκρολογήστε τον πρώτο αριθμό του διαστήματος")
 if diast1 !="":
    diast1=int(diast1)
    diast2 = int(input("πληκρολογήστε τον δεύτερο αριθμό του διαστήματος"))
    list_f.append([diast1,diast2])
 print("πληκρολογήστε "" για να σταματήσετε την εκχώρηση.")       
 print (list_f)



def sumIntervals(list_f):
   array_length = len(list_f)  
   for i in range(array_length):
      for j in range(array_length):
       if i!=j:
         a=(list_f[i][1])-(list_f[j][1]) #CASE1    if the new interval is going to have a new maximum number       (if the max number of an interval is bigger than the max number of the other interval)
         b=(list_f[j][1])-(list_f[i][0]) #Check that CASE1 is not going create new interval from intervals they dont belong in each other
         c=(list_f[i][1])-(list_f[j][0]) #CASE2    if the new interval is going to have a new minimum number
         #Check if an interval is [0,0]
         zeroCheck1=1
         zeroCheck2=1
         if list_f[i][1]==0 and list_f[i][0]==0:
           zeroCheck1=0
         if list_f[j][1]==0 and list_f[j][0]==0:
           zeroCheck2=0    
         if  a>0 and b>=0  and zeroCheck1==1 and zeroCheck2==1 :   #CASE1 
           list_f[i][0]=list_f[j][0]
           list_f[j][0]=0
           list_f[j][1]=0
         elif  c>0  and list_f[j][1]>list_f[i][1]  and zeroCheck1==1 and zeroCheck2==1:    #CASE2
            list_f[i][1]=list_f[j][1]
            list_f[j][0]=0
            list_f[j][1]=0
   print(list_f)
   sum=0
   for i in range(array_length):
      sum=sum+(list_f[i][1])-(list_f[i][0])
   print ("το άθροισμα των διαστημάτων είναι:",sum)   

sumIntervals(list_f)  
