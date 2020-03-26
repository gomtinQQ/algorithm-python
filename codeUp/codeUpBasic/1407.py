'''
1407 : 문자열 출력하기 1
길이(글자수)가 100이하인 문자열을 입력받아 공백을 제거하고 출력하시오.
'''
# 방법 1
myString = input()
list = myString.split(" ")
answer = ''.join(list)
print(answer)

# 방법 2
import re
print(re.sub(' ', '', myString))