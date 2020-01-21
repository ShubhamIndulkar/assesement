import csv
with open("input.csv","rt") as file:
     input_file = csv.reader(file)
    # output_file = csv.writer("output.csv")
     n = []
     for row in input_file:
         n.append(row)
     out=[]
     for i in range(1,len(n)):
         a=n[i][1]
         b=n[i][2]
         sum=0
         if n[i][6]=="Y":
             sum=sum+500
         elif n[i][6]=="N":
             if n[i][3]=="SELL" or n[i][3]=="WITHDRAW":
                 sum=sum+100
             else:
                 sum=sum+50

         for j in range(1,len(n)):
             if n[j][1]==a and n[j][2]==b:
                 if n[j][4]==n[i][4]:
                     if n[j][3]=="SELL" and n[i][3]=="BUY" or n[j][3]=="BUY" and n[i][3]=="SELL" or n[j][3]=="WITHDRAW" and n[i][3]=="DEPOSIT" or n[j][3]=="DEPOSIT" and n[i][3]=="WITHDRAW":
                         sum=sum+10
                     else:
                         sum=sum+0
         out.append(sum)
     print(out)
     print(len(out))
     list1=[]
     for i in range(1, len(n)):
         list1.append([n[i][1], n[i][3], n[i][4], n[i][6], out[i - 1]])
         list2=(sorted(list1, key=lambda x: (x[0], x[1],x[2],x[3])))

    # print(sorted(list1, key=lambda x: (x[0], x[1],x[2],x[3])))


with open('output.csv', 'w', newline='') as file:
     writer = csv. writer(file)
     writer.writerow(["Client id ","Transaction Type ","Transaction Date"," Priority flag","Processing Fee"])
     for i in list2:
         writer.writerow(i)



Sapient code
Reply all
Forward
Verma, Sahil C.
Mon 20-01-2020 15:43
