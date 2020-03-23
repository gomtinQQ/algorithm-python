'''
1675 : 씨저의 암호 1
암호학에서 씨저 암호(Caesar cipher)는 가장 오래된 암호이고 가장 대표적인 대치(substitution) 암호로서 평문 문자를 다른 문자로 일대일 대응시켜 암호문을 만들어 내는 방식이다.
씨저 암호는 알파벳을 3글자씩 밀려서 쓰면서 문장을 만들었다.
실제 씨저는 부하인 브루투스에게 암살되기 전에 키케로에게 다음과 같은 암호문을 보냈다고 한다.
qhyhu wuxvw euxwxv
===> never trust brutus    (절대 부루투스를 믿지마라)
원리는 간단하다. 3작은 알파벳으로 치환하면 된다.
암호 - A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
평문 - X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
씨저의 암호문이 주어지면 평문으로 복원하는 프로그램을 작성하시오.
'''
# a = 97, z = '122'
cipher = input()
str_list = []
answer_list = []

# 암호문을 한글자씩 슬라이싱한다.
for i in range(len(cipher)):
    str_list.append(cipher[i])

# 암호문을 해석한 뒤 answer_list에 넣는다.
for i in range(len(str_list)):
    if(97<=ord(str_list[i])<=99):
        answer_list.append(ord(str_list[i])+23)

    elif(str_list[i]==' '):
        answer_list.append(' ')

    else:
        answer_list.append(ord(str_list[i])-3)

# 평서문을 출력한다.
for i in range(len(answer_list)):
    if(answer_list[i]==' '):
        print(answer_list[i], end="")
    else:
        print(chr(answer_list[i]), end="")
