a=lambda x:x+3
print("O/P is",a(4))
l=[1,2,3,4,5]
def even(x):
    if(x%2==0):
        print("even",x)
    else:
        return False

l1=list(filter(a,l))

l2=list(map(a,l))
print(l2)