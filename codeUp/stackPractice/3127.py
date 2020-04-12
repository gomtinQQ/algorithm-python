'''
3127 : 수식 계산 1
3 5 7 ∗+
6 9 +8∗
이다.
후위 표기법은 연산자의 순서가 곧 계산 순서이므로 괄호가 필요 없다는 장점이 있다.
후위 표기법으로 된 식을 입력 받아 계산 결과를 출력하는 프로그램을 작성하시오.
'''
import mystack
cal_lst = input().split()
s = mystack.CustomStack()
tmp = 0

for i in cal_lst:
    if(i.isnumeric()):
        s.push(int(i))
    elif(i==" "):
        pass
    else:
        s1 = s.pop()
        s2 = s.pop()
        if(i=="*"):
            tmp = s2*s1
        elif(i=="/"):
            tmp = int(s2/s1)
        elif(i=="+"):
            tmp = s2+s1
        else:
            tmp = s2-s1
        s.push(tmp)

print(s.pop())


