'''
3102 : STL stack
피어나라 꿈나무들은 오늘 스택에 대해 공부할 것이다.
STL stack명령어를 익힐 수 있도록 해보자.
N개의 명령어가 입력되면, 순서대로 동작하는 프로그램을 제작하시오.
명령어 설명 :
push( x ) : x를 스택에 넣는다.(x는 정수) 괄호와 x사이에 공백이 반드시 존재한다.
top() : 스택의 top 포인터가 가리키는 값을 출력한다.  만약 원소가 없다면 -1을 출력한다.
pop() : 스택의 마지막에 들어온 원소를 삭제한다.
size() : 스택안의 원소 개수를 출력한다.
empty() : 스택이 비어있으면 true, 비어 있지 않으면 false 를 출력한다.
'''
import mystack

s = mystack.CustomStack()
n = int(input())
x = 0

for i in range(n):
    state = input()
    tmp = state[:2]

    if tmp == "pu":
        x = int(state[6:-1])
        s.push(x)
    elif tmp == "po":
        s.pop()
    elif tmp == "si":
        print(s.size())
    elif tmp == "to":
        print(s.top())
    elif tmp == "em":
        if s.is_empty() == True:
            print("true")
        else:
            print("false")