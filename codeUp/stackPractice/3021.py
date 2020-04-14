'''
3021 : 큰 수 덧셈
int는 32비트, long long 은 64비트라서 이 보다 더 큰 숫자는 저장할 수 없다.
아주 큰 숫자의 덧셈을 하려고 한다.
계산 결과를 출력하시오.
'''
class CustomStack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if(self.is_empty()):
            return 0
        else:
            return self.stack.pop()

    def push(self, item):
        return self.stack.append(item)

    def is_empty(self):
        if(len(self.stack)==0):
            return True
        else:
            return False

    def size(self):
        return len(self.stack)

def addNum(num1, num2):
    # num1이 큰 수, num2가 작은 수
    min = 0
    if num1 < num2:
        min = num1
        num1 = num2
        num2 = min

    num1 = str(num1)
    num2 = str(num2)
    carry = 0
    s1 = CustomStack()
    s2 = CustomStack()
    rs = CustomStack()

    for i in num1:
        s1.push(i)
    for i in num2:
        s2.push(i)

    while(s1.is_empty()!=True):
        tmp = 0
        if carry == 1:
            tmp = int(s1.pop()) + int(s2.pop()) + 1
            carry = 0
            if tmp >= 10:
                carry = 1
                tmp -= 10
        else:
            tmp = int(s1.pop()) + int(s2.pop())
            if tmp >= 10:
                carry = 1
                tmp -=10
            else:
                carry = 0
        rs.push(tmp)

    if carry == 1:
        rs.push(1)

    while(rs.is_empty()!=True):
        print(rs.pop(), end="")

num1 = int(input()) # 큰 수
num2 = int(input()) # 작은 수

addNum(num1, num2)