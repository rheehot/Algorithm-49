#10430
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
expr1 = (A+B)%C
expr2 = ((A%C)+(B%C))%C
expr3 = (A*B)%C
expr4 = ((A%C)*(B%C))%C
print(expr1)
print(expr2)
print(expr3)
print(expr4)
