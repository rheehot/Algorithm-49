# 2588
a = input()
b = input()
a = int(a)
b = int(b)
one = a*(b%10)  #나머지 연산자로 1의 자리 값 구하기
hundred = a*(int(b/100)) # 나누기 연산자와 정수형 변환으로 100의 자리 값 구하기
ten = a*((int(b/10))%10) # 나눗셈,나머지 연산자 + 정수형 변환으로 10의 자리값 구하기
result = hundred*100 +ten*10 + one
print(one)
print(ten)
print(hundred)
print(result)
