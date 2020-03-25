'''
1403 : 배열 두번 출력하기
k개의 숫자를 입력받고 그 숫자들을 두번 출력하시오.

입력 예)
2
5 7
출력 예)
5
7
5
7
'''
n = int(input())
list = input().split()

for i in range(2):
    for j in range(len(list)):
        print(list[j])