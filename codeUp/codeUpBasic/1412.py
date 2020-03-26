'''
1412 : 알파벳 개수 출력하기
어떤 영어 문장이 주어지면 각 알파벳이 몇 번 나왔는지 출력하시오.
'''
import string
sentence = input()
alphabet = list(string.ascii_lowercase)
mydict = {}

# dictionary 생성
for i in range(len(alphabet)):
    key = alphabet[i]
    mydict[key]=0

# 해당 알파벳이 나오면 count를 증가시킨다.
for i in range(len(sentence)):
    if(97<=ord(sentence[i])<=122):
        mychar = sentence[i]
        mydict[mychar] = (mydict[mychar] + 1)

for i in range(97, 123):
    mychar = chr(i)
    print("{0}:{1}".format(mychar, mydict[mychar]))