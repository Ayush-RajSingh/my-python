
fruits=["mango","grapes","apple","apple","orange"]
name = input("enter name")

if (name in fruits): 
    print("name is present")
else:
    print("name is not present ")
    dupfruits = [] #empty list 
for s in fruits:
    if(s not in dupfruits) :
        dupfruits.append(s)

print(dupfruits)       

fruits = []

while(True):
    n = input(" enter fruit name")
    fruits.append(name)
    ch = input("do you want to write more yes or no")
    if(ch == yes):
        n
    else:
        break 




#3sfruits = set(fruits)
#fruits = list(sfruits)

#print(fruits)
#print(list(dict.fromkeys(fruits)))

#fruits=["mango","grapes","apple","apple","orange"]
#print("Original List: ", fruits)
#res = [*set(fruits)]
#print("List after removing duplicate elements: ", res)