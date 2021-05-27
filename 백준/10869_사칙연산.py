# 백준 10869

a, b = input().split()
a = int(a)  # 문자열을 정수로 형변환
b = int(b)
print(a+b)  #덧셈
print(a-b)  #뺄셈
print(a*b)  #곱셈
print(int(a/b))  #나눗셈, python3부터는 정수끼리 나누면 실수가 나온다.따라서 형 변환 함수 int()를 사용하여 몫을 구한다.
print(a%b)  #나머지
