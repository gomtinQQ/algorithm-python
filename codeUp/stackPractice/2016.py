'''
2016 : 천단위 구분기호
우리는 흔히 숫자를 쓸때 천단위 구분기호인 콤마(,)를 많이 쓴다.
숫자가 입력되면 천단위 구분기호를 넣어 숫자를 출력하시오.
'''
import mystack
s = mystack.CustomStack()
cnt = 0
n = int(input())
num = input()

if n <= 3:
    print(int(num))
else:
    for i in reversed(num):
        cnt += 1
        if(cnt%3==0 and cnt < n):
            s.push(i)
            s.push(",")
        else:
            s.push(i)

while (s.is_empty() != True):
    print(s.pop(), end="")





