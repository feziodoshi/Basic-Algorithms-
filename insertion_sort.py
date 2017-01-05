A=[1,2,6,1,4,3]
##key is the element that is going to be sorted everytime


##like cards you pick a card and start sorting fropm the second card

for i in range(1,len(A)):
    key=A[i]
    j=i-1
    while(j>=0 and A[j]>key):
        A[j+1]=A[j]
        j=j-1
    A[j+1]=key
    
        
