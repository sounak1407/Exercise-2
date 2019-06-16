list=[8,6,9,2,3]
print(list)
n=int(input("1.Enter 1 for ascending \n2.Enter 2 for descending\n "))

#Descending order:
if n==2:
    for i in range(5):
        j=i+1
        for j in range (5):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
#Ascending order:
elif n==1:
    for i in range(5):
        j=i+1
        for j in range (5):
            if list[i]<list[j]:
                list[i],list[j]=list[j],list[i]
#Invalid input:
else:
    print("Enter is invalid:try again")

print(list)