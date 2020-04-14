'''
3022 : 큰 수 뺄셈
'''
class CustomStack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        return self.stack.append(item)

    def pop(self):
        if(self.is_empty()):
            return 0
        else:
            return self.stack.pop()

    def is_empty(self):
        if len(self.stack)==0:
            return True
        else:
            return False

def subNum(num1, num2):
    # 큰 수가 num1, 작은 수가 num2
    f = 0
    if num2 > num1:
        min = num1
        num1 = num2
        num2 = min
        f = 1

    s1 = CustomStack()
    s2 = CustomStack()
    rs = CustomStack()
    carry = 0
    result = ""

    for i in str(num1):
        s1.push(i)
    for i in str(num2):
        s2.push(i)

    while(s1.is_empty()!=True):
        tmp = 0
        if carry == 1:
            tmp = int(s1.pop()) - int(s2.pop()) - 1
            carry = 0
            if tmp < 0:
                tmp += 10
                carry = 1

        else:
            tmp = int(s1.pop()) - int(s2.pop())
            if tmp < 0:
                tmp += 10
                carry = 1
        rs.push(tmp)

    while(rs.is_empty()!=True):
        result = result + str(rs.pop())

    if f == 1:
        result = -(int(result))
    else:
        result = int(result)

    return result

num1 = int(input())
num2 = int(input())
print(subNum(num1, num2))