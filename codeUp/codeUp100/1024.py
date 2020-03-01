'''
1024 : [기초-입출력] 단어 1개 입력받아 나누어 출력하기(설명)

단어를 1개 입력받는다.
입력받은 단어(영어)의 각 문자를한줄에 한 문자씩 분리해 출력한다.

INPUT
Boy

OUTPUT
'B'
'o'
'y'

'''
myWord = input()
myCharList = list(myWord)

#철자 하나씩 출력하기
for c in myCharList:
    print("\'" + c + "\'")
