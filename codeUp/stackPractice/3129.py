'''
3129 : 올바른 괄호 2
여는 괄호와 닫는 괄호의 개수만으로는 올바른 괄호 문자열을 판단할 수 없다.
예를 들어, )()( 이런 문자열도 개수는 같지만 올바른 괄호 문자열이 아니다.
어떤 괄호 문자열이 주어지면 올바른 괄호 문자열인지 판단하시오.
올바른 괄호 문자열이면 "good", 올바른 괄호 문자열이 아니면 "bad"를 출력하시오.
'''
class CustomStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        return self.stack.append(item)

    def pop(self):
        if (self.is_empty()):
            return -1
        else:
            return self.stack.pop()


    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

lst = list(input())
open = CustomStack()
result = True

if lst[0] == ')':
    result = False
else:
    for i in lst:
        if(i=='('):
            open.push(i)
        else:
            if open.pop() == -1: # open 수 보다 close 수가 더 많을 때 bad
                result = False
                break
    # close 괄호 만큼 open.pop() 진행 후 open 괄호가 남았을 경우 bad
    if(open.is_empty()!=True):
        result = False

if result == False:
    print("bad")
else:
    print("good")
