A=[]
B=[]
print("Elements for A :")
a=input().strip().split()
for i in a:
    A.append(int(i))
print("Elements for B :")
b=input().strip().split()
for i in b:
    B.append(int(i))
distance=0
for i in range(len(A)):
    distance+=abs(A[i]-B[i])
print("First array",A)
print("First array",B)
print("Manhatten distance : ",distance)


