''' In second year computer engineering class, group A students play cricket, group B
    students play badminton and group C students play football.
    Write a Python program using functions to compute following: -
    a) List of students who play both cricket and badminton
    b) List of students who play either cricket or badminton but not both
    c) Number of students who play neither cricket nor badminton
    d) Number of students who play cricket and football but not badminton.
    (Note- While realizing the group, duplicate entries should be avoided, Do not use SET
    built-in functions)'''




def func(a):
    l=[]
    for i in a:
        if not i in l:
            l.append(i)
    return l



SEComp =[]

n = int(input("\nEnter number of students in SE COMP: "))
print("Enter the names of",n,"students :")
for i in range(0, n):
    x = input()
    SEComp.append(x)
print("Original list of students in SEComp : " + str(SEComp))

Cricket =[]
n = int(input("\n\nEnter number of students who play cricket : "))
print("Enter the names of",n,"students who play cricket : ")
for i in range(0, n):
    y = input()
    Cricket.append(y)
print("Original list of students playing cricket is :" +str(Cricket))

badminton =[]
n = int(input("\n\nEnter number of students who play badminton : "))
print("Enter the names of",n,"students who play badminton : ")
for i in range(0, n):
    y = input()
    badminton.append(y)
print("Original list of students playing badminton is :" +str(badminton))

football =[]
n = int(input("\n\nEnter number of students who play football : "))
print("Enter the names of",n,"students who play football : ")
for i in range(0, n):
    y = input()
    football.append(y)
print("Original list of students playing football is :" +str(football))

#List of students who play both cricket and badminton
c_b=[]
for i in Cricket:
    for j in badminton:
        if i ==j:
            c_b.append(i)
        else:
            pass
print("List of students who play both cricket and badminton:",c_b)

#List of students who play either cricket or badminton but not both

only_cb=[]


for i in Cricket:
    if i not in badminton:
        only_cb.append(i)
for i in badminton:
    if i not in Cricket:
        only_cb.append(i)

print(" List of students who play either cricket or badminton but not both:",only_cb)

#Number of students who play neither cricket nor badminton

nc_nb=[]
for i in football:
    nc_nb.append(i)

for i in Cricket:
    for j in nc_nb:
        if i==j:
            nc_nb.remove(i)

for i in badminton:
    for j in nc_nb:
        if i==j:
            nc_nb.remove(i)

print("Number of students who play neither cricket nor badminton",nc_nb)

#Number of students who play cricket and football but not badminton.


fc_f_nb=[]
for i in Cricket:
    for j in football:
        if i==j:
            fc_f_nb.append(i)

for i in fc_f_nb:
    for j in badminton:
        if i==j:
            fc_f_nb.remove(i)

print("Number of students who play cricket and football but not badminton:", fc_f_nb)








