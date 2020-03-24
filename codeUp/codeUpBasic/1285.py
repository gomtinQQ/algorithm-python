'''
1285 : 계산기 2
계산기 1에서 두 피연산자에 대한 연산만 다루었다.
이번에는 식을 입력하면 차례대로 계산하여 출력하는 계산기를 만들어보자.
단, 우선순위는 따지지 않고 왼쪽에서 부터 차례대로 계산하고, 모든 계산은 정수형 계산으로 처리한다.
'''
list = input()
num_list = []
op_list = []
lastIndex = 0

# number과 operator를 분리한다
for i in range(len(list)):
    if(list[i] in ('+','-','*','/','=')):
        op_list.append(list[i])
        num_list.append(int(list[lastIndex:i]))
        lastIndex = i+1

result = num_list[0]

# calculate
for i in range(len(op_list)):
    if(op_list[i]=='+'):
        result = result + int(num_list[i+1])
    elif(op_list[i]=='-'):
        result = result - int(num_list[i+1])
    elif(op_list[i]=='/'):
        result = int(result / int(num_list[i+1]))
    elif(op_list[i]=='*'):
        result = result * int(num_list[i+1])

print(result)
