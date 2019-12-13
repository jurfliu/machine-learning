#1.list
list=[2,3,4,5,6]
for k in list:
    print(k,end=",");
print([x for x in list]);
print("")
#2.rnage
for i in range(2,10):
    print(i,end=",")
print("")
#3,zip
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for index ,item in zip(list_a,list_b):
    print(index,item)
print("")
#4.index
for index ,item in enumerate(list):
    print(index,item)

