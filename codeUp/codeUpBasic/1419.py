'''
1419 : love 2
영어 문장이 입력된다.
그 문장에서 love가 몇 번 나오는지 출력하시오.
'''
sentence = input()
cnt = 0

for i in range(len(sentence)):
    if(sentence[i:i+4]=='love'):
        cnt+=1

print(cnt)