import scipy as sp
print(sp.convolve([1,2,3,4],[4,5,6]));
def convDemo(lst1,lst2):
    length1=len(lst1)
    length2=len(lst2)
    lst1.reverse()
    result=[]
    print(lst1)
    for i in range(1, length1 + 1):
        t = lst1[length1 - i:]  # str1=[1,2,3,4]  str2=[4,5,6]
        print("t:",t)
        re1 = [item1 * item2 for item1, item2 in zip(t, lst2)];
        re1 = sum([item1 * item2 for item1, item2 in zip(t, lst2)])
        result.append(re1)
    for i in range(1, length2):
        t = lst2[i:]
        print("t2:",t)
        re2 = sum([item1 * item2 for item1, item2 in zip(lst1, t)])
        print("re2:",re2)
        result.append(re2)
    return result
result=convDemo([1,2,3,4],[4,5,6])
print(result)

#执行流程
'''

#1
list1=[4,3,2,1]
    t=[1]
list2=[4,5,6]
item=1,item2=4;
[item*item2]=[1*4]=[4]
sum([item*item2])=4
#2
list1=[4,3,2,1]
    t=[2,1]
list2=[4,5,6]
item=2,1,item2=4,5;
[item*item2]=[2*4,1*5]=[8,5]
sum([item*item2])=8+5=13
#3

list1=[4,3,2,1]
    t=[3,2,1]
list2=[4,5,6]
item=3,2,1,item2=4,5,6;
[item*item2]=[3*4,2*5,1*6]=[12,10,6]
sum([item*item2])=12+10+6=28

#4
list1=[4,3,2,1]
    t=[4,3,2,1]
list2=[4,5,6]
item=4,3,2,1,item2=4,5,6;
[item*item2]=[4*4,3*5,2*6]=[16,15,12]
sum([item*item2])=16+15+12=43



list1=[4,3,2,1]
    t=[5,6]
list2=[4,5,6]

==>4*5+3*6=38

list1=[4,3,2,1]
    t=[6]
list2=[4,5,6]

==>4*6=24



'''