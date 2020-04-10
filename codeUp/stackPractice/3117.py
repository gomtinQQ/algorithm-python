'''
3117 : 0은 빼!
당신의 상관은 당신이 작년에 회사의 실적에 얼마나 도움이 되었는지 횟수를 세었다.
불행히도 당신의 상관은 때때로 횟수를 틀리게 읽는다.
다행히도 당신의 상관은 잘못된 숫자를 읽은 것을 인식하면 ‘zero’라고 말한다. 이는 ‘직전의 숫자는 무시한다’는 것을 의미한다.
불행히고 당신의 상관은 실수를 반복할 수 있고, 매 실수 마다 ‘zero’라고 말한다.
어느 순간이나 당신의 상관은 ‘zero’라고 말할 수 있으며, 만약 모든 숫자들이 무시되면 그 합은 0이 된다.
'''
import mystack
s = mystack.CustomStack()
result = 0

n = int(input())
for i in range(n):
    tmp = int(input())
    if(tmp==0):
        s.pop()
    else:
        s.push(tmp)

while(s.is_empty()!=True):
    result = result + s.pop()

print(result)