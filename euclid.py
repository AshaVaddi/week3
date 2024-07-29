import math

A = []
B = []

print("Enter elements for A (space-separated):")
a = input().split()
for i in a:
    A.append(int(i))

print("Enter elements for B (space-separated):")
b = input().split()
for i in b:
    B.append(int(i))

if len(A) != len(B):
    print("Error: Both lists must have the same number of elements.")
else:
    distance = 0
    for i in range(len(A)):
        distance += (A[i] - B[i]) ** 2
    distance = math.sqrt(distance)

    print("First array:", A)
    print("Second array:", B)
    print("Euclidean distance:", distance)
