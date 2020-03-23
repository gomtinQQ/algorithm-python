'''
1294 : 씨저의 암호 2
대현이는 씨저의 암호 방식을 이용하여 문장을 만들려고 한다.
never trust brutus 를 씨저의 암호로 바꾸면 qhyhu wuxvw euxwxv 이다.
(1675 참고)씨저 암호는 알파벳을 3글자씩 밀려서 쓰면서 문장을 만들었다.
'''
text = input()
str_list = []
cipher = []

# text를 한 글자씩 슬라이싱하여 str_list에 넣는다.
for i in range(len(text)):
    str_list.append(text[i])


# text -> cipher 암호로 변환
for i in range(len(str_list)):
    if(120<=ord(str_list[i])<=122):
        cipher.append(ord(str_list[i])-23)
    elif(str_list[i]==' '):
        cipher.append(' ')
    else:
        cipher.append(ord(str_list[i])+3)

# cipher 출력
for i in range(len(cipher)):
    if(cipher[i]==' '):
        print(' ', end="")
    else:
        print(chr(cipher[i]), end="")


