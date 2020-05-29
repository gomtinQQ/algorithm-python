'''
문제: 핸드폰 번호 가리기
'''
def solution(phone_number):
    return "*" * (len(phone_number)-4) + str(phone_number[-4:])