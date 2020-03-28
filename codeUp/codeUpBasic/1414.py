'''
1414 : C언어를 찾아라
길이가 100 이하인 문자열로 구성된 암호문을 발견하였다.
이 암호문은 예전에 작성된 것으로 판단된다.
이 문자열에서 “C”라는 문자와 “CC”라는 문자가 몇 개 있는지 조사하고자 한다.
길이가 100 이하인 문자열을 입력받아, "C"라는 문자와 "CC"라는 문자가 각각 몇 개 존재하는지 알아내는 프로그램을 작성하시오. (단, C, CC는 대소문자를 구분하지 않는다. 즉, "cC"는 "CC"와 같다.)
'''
str_list = input()
str_upper = str_list.upper()
cc_cnt = 0

for i in range(0, len(str_upper)):
    if str_upper[i]=='C':
        if(i!=len(str_upper)-1 and str_upper[i+1]=='C'):
            cc_cnt+=1

print(str_upper.count('C'))
print(cc_cnt)