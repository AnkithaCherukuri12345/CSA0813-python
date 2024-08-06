#square
n=5
for i in range(1,6):
    for j in range(1,6):
        print('*',end=" " )
    print()
    
 #diamond       
n=4
for i in range(1,5):
    print(' '*(n-i)+'*'*(2*i-1))
n=4
for i in range(3,0,-1):
    print(' '*(n-i)+'*'*(2*i-1))


#rectangle
m=3
n=5
for i in range(m):
    for j in range(n):
        print('*',end=" ")
    print()

 
#triangle
n=5
for i in range(1, 6):
    print('*'*i)

    
#hallow square
n=4
for i in range(1,5):
    for j in range(1,5):
        if (i==1 or i==n or j==1 or j==n):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

    
#inverted triangle

n=5
for i in range(5,0,-1):
    print('*'*i)
