'''
1261 : First Special Judge (Test)
10개의 수가 입력된다.
10개의 수 중 5의 배수를 하나만 출력한다.
만약 5의 배수가 없다면 0을 출력한다.
'''
number = input().split()
cnt = 0
for i in range(len(number)):
    if(int(number[i])%5==0):
        print(number[i])
        cnt+=1
        break

if(cnt==0):
    print(0)