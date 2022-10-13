n=int(input("enter number:"))
for i in range((-n+1),n+1):
    x=n-abs(i)
    print("   "*(n-x),end="")
    for j in range(1,x+1):
        if j==1 or j==x:
            print("  *  ",end="")
        else:
            print("   ",end="")
    print("")
