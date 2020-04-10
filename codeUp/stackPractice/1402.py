'''
1402 : 거꾸로 출력하기 3
두 수를 거꾸로 출력하기..
세 수를 거꾸로 출력하기...
이런 문제들은 쉽게 풀 수 있었다.
이번에는 데이터의 개수가 n개가 들어오고, n개의 데이터를 거꾸로 출력하는 프로그램을 작성하시오.

n = int(input())
n_lst = list(map(int, input().split()))

for i in range(len(n_lst)):
    print(n_lst.pop(), end=" ")
'''
import mystack
s = mystack.CustomStack()

n = int(input())
n_lst = input().split()

for i in n_lst:
    s.push(int(i))

while(s.is_empty()!=True):
    print(s.pop(), end = " ")



