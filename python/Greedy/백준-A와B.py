A = list(input())
B = list(input())

while len(B) > len(A):
    if B[len(B) - 1] == 'A':
        B = B[:len(B) - 1]
    else:
        B = B[:len(B) - 1]
        B = B[::-1]
    
A_str = ''
B_str = ''

for i in range(0, len(A)): A_str += A[i]
for i in range(0, len(B)): B_str += B[i]

if A_str == B_str:
    print(1)
else:
    print(0)