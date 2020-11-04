#a=int(input("Enter the value"))
#b=int(input("Enter the second value"))
#c=a+b
#print(c)
list=["A","B","C","D"]
x=len(list)
for i in range(x):
    print(i)
list.append("hello")
print(list)
list.insert(5,"hii")
print(list)
c=len(list)
print(c)
li=[1,2,3,4]
li.extend(list)
print(li)
