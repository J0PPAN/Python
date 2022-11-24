L = []
k=0
while k == 0:
    x = int(input("Enter the array elements one by one : "))
    L.append(x)
    k = int(input("Do you want to continue[0/1] : "))
    if k != 0:
        break

def Bubble(L):                                                                                                                                               
    print("\n\t\tBubble Sort Using Function Definition")
    print("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    N=len(L)
    print("Original list: ", L )
    for i in range(N-1):       
        for j in range(N-i-1):
            if L[j] > L[j+1]:                                                                   
                L[j] , L[j+1] = L[j+1] , L[j]                                               
    print("New List After Performing Bubble sort: ", L )       

Bubble(L)     
