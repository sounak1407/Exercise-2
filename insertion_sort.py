arr=[65,25,15,35,20]


for i in range(1,len(arr)):
 sort=i
 j = i - 1
 while j>=0 and arr[sort]<arr[j]:

     arr[j+1]=arr[j]
     j -= 1
 arr[j+1]=arr[sort]



print(arr)