'''
1024 : [기초-입출력] 단어 1개 입력받아 나누어 출력하기(설명)
단어를 1개 입력받는다.
입력받은 단어(영어)의 각 문자를
한줄에 한 문자씩 분리해 출력한다.
'''
word = input()
word_list = list(word)

for i in range(len(word_list)):
    print("\'{0}\'".format(word_list[i]))