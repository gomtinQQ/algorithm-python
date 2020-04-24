'''
문제: 다트 게임
다트 게임은 총 3번의 기회로 구성된다.
1. 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
2. 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
3. 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
4. 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
5. 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
6. 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
7. Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
8. 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
9. 0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.

|점수|보너스|[옵션]
'''
s = list(input())
score = []
lst = []
for i in s:
    if i.isdigit():
        if len(lst)!=0 and str(lst[-1]).isdigit():
            lst[-1] = int(str(lst[-1]) + str(i))
        else:
            lst.append(int(i))
    else:
        lst.append(i)

for i in range(len(lst)):
    x = lst[0]
    del lst[0]

    if str(x).isdigit():
        score.append(x)
    elif x == 'S':
        score[-1] = score[-1]
    elif x == 'D':
        score[-1] = score[-1] ** 2
    elif x == 'T':
        score[-1] = score[-1] ** 3
    elif x == '*':
        score[-1] = score[-1] * 2
        if len(score) != 1:
            score[-2] = score[-2] * 2
    elif x =='#':
        score[-1] = score[-1] * (-1)

print(sum(score))


