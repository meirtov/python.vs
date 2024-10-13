new_num=0 
num = float(input("float number")) 
binum = int(input("bin"))
new_bin= [0]  * binum
if num>9:
    for i in range(binum , 0 , -1):
        if num>pow(2,i) and num<pow(2,i+1):
            new_num=num-pow(2,i)
            new_bin[i]=1
        else :
             new_bin[i]=0
else:
     print("wrong")
print(new_bin)
newmin=[0] * binum
for i in range(binum):
    if new_bin[i]==1:
      newmin[i]=0
    else :
        newmin[i]=1
newmin[0]=1
for i in range(binum):
    print(newmin[i])
