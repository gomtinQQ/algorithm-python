'''
1046 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기
정수 3개를 입력받아 합과 평균을 출력해보자.
단, -2147483648 ~ +2147483647
'''
x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

sum = x+y+z
avg = round(sum/3, 1)

print(sum)
print(avg)