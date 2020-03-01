'''
년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.
연, 월, 일이 ".(닷)"으로 구분되어 입력된다.
input : 2013.1.1
output : 2013.01.01
'''
y, m, d = input().split('.')
print("%04d" % int(y), end='.')
print("%02d" % int(m), end='.')
print("%02d" % int(d))
