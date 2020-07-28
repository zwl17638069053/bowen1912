a = [12,5,3,7,4,8,9]
for i in range(len(a)):
    for j in range(len(a)-1):
         if a[i]<a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            print(a)