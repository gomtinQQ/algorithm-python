'''
1714 : 숫자 거꾸로 출력하기
현우는 숫자를 좋아한다. 항상 숫자를 가지고 장난을 하고 숫자로 무언가 만들기를 취미생활로 즐기고 있다.
하루는 어떤 숫자를 쓰고, 그 수를 거꾸로 쓰기로 했다.
어떤 수 N이 입력되면 그 수를 거꾸로 출력하는 프로그램을 작성하시오.

예)
입력 : 2571
출력 : 1752
입력 : 1200
출력 : 0021
'''
import mystack
s = mystack.CustomStack()
num = list(input())
r_num = ""

for i in num:
    s.push(int(i))

while(s.is_empty()!=True):
    r_num = r_num + str(s.pop())

print(r_num)
