'''
1254 : 알파벳 출력하기
시작 알파벳과 마지막 알파벳을 입력받아 그 두 알파벳 사이의 모든 알파벳을 출력하시오.
예) a f   ====> a b c d e f
'''
x, y = input().split()
x = ord(x)
y = ord(y)
if(x>y):
    min = y
    max = x
else:
    min = x
    max = y
for i in range(min, max+1):
    print(chr(i), end=" ")
