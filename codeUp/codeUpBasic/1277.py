'''
1277 : 몇 번째 데이터 출력하기
첫 줄에 데이터의 개수 N(N은 홀수)이 입력되고, 그 다음 줄에 N개의 데이터가 입력된다.
여기서 첫번째 데이터, 중간 데이터, 마지막 데이터를 출력하시오.
예)
5
2 4 6 1 7
이면
2 6 7
이 출력된다.
(첫번째 데이터 2, 중간 데이터 6, 마지막 데이터 7)
'''
N = int(input())
num_list = list(map(int, input().split()))
mid = int(N/2)

print("{0} {1} {2}".format(num_list[0], num_list[mid], num_list[N-1]))
