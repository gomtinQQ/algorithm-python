'''
1408 : 암호 처리
[어떤 인터넷 서비스의 2가지 암호화 방법]
- 입력받은 문자의 ASCII 코드값 + 2
- (입력받은 문자의 ASCII 코드값 * 7) % 80 + 48
사용자의 패스워드를 2가지 방법으로 암호화한 결과를 출력하는 프로그램을 작성하시오.
'''
pwd = input()
for i in range(len(pwd)):
    print(chr(ord(pwd[i])+2), end="")
print()

for i in range(len(pwd)):
    print(chr((ord(pwd[i])*7)%80+48), end="")
