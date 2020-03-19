'''
1265 : 구구단 출력하기 1
구구단의 원하는 단을 입력하면 그 단의 구구단이 출력되게 하시오.
'''
n = int(input())
for i in range(1, 10):
    print(str(n) + "*" + str(i) + "=" + str(n*i))