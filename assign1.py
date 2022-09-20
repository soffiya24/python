#Title : implementation SET operations on array linear data structure
#grp_c=group of cricket playing student
#grp_b=group of badminton playing student
#grp_f=group of football playing student
#List of students who play both cricket and badminton
n=int(input("enter no. of student for cricket"))
m=int(input("enter no. of student for badminton:")) 
p=int(input("enter no. of student for football:")) 
grp_c=[]
grp_b=[]
grp_f=[]
for i in range(1,n+1):
  name_c=input("enter name of cricket playing student:")
  grp_c.append(name_c)
for j in range(1,m+1):  
  name_b=input("enter name of badminton playing student:")
  grp_b.append(name_b)    
for k in range(1,p+1):  
  name_f=input("enter name of football playing student:")
  grp_f.append(name_f)
print("students playing cricket:  ",grp_c)
print("students playing badminton:  ",grp_b)
print("students playing football:  ",grp_f)
#students playing both cricket and badminton
bothCB=[]
lenC=len(grp_c)
lenB=len(grp_b)
for i in range(lenB):
  for j in range(lenC):
    if grp_b[i]==grp_c[j]:
      bothCB.append(grp_b[i])
print(bothCB) 
#students playing either cricket or badminton noth both
CorB=[]
f=0
lenC=len(grp_c)
lenB=len(grp_b)
for i in range(lenB):
  for j in range(lenC):
    if(grp_b[i]==grp_c[j]):
      f=1
  if f==0:
    CorB.append(grp_b[i])
  else:
    f=0
for i in range(lenC):
  for j in range(lenB):
    if(grp_c[i]==grp_b[j]):
      f=1
  if f==0:
    CorB.append(grp_c[i])
  else:
    f=0
print(CorB)
#students playing neither cricket not badminton
only_f=grp_f
for i in grp_f:
  if i in (grp_c or grp_b):
    only_f.remove(i)
print(only_f)
#students playing cricket and football but not badminton
Union=grp_c+grp_f
for i in Union:
  if i in grp_b:
    Union.remove(i)
print(Union)
