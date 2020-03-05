''''
1076 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)
영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.

'''
myChar = input()
#x는 마지막 문자를 의미하는 숫자이다
firstCharNumber = ord('a')
myCharNumber = ord(myChar)

list = (range(firstCharNumber,myCharNumber+1))
for i in list:
    myChar = chr(i)
    print(myChar)