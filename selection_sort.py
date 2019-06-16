arr=[24,32,12,2,14,6]
print(arr)
n=int(input("1.Enter 1 for ascending \n2.Enter 2 for descending\n "))
#Ascendding order
if n==1:
 for i in range(len(arr)):
    min=i
    for j in range(i+1,len(arr)):
        if arr[min]>arr[j]:
            min=j

    arr[i],arr[min]=arr[min],arr[i]
#Descending order
elif n==2:
 for i in range(len(arr)):
    max=i
    for j in range(i+1,len(arr)):
        if arr[max]<arr[j]:
            max=j

    arr[i],arr[max]=arr[max],arr[i]
else:
    print("Invalid input")
print("sorted array :",arr)
