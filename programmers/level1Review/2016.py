'''
문제: 2016년
'''
import datetime as dt
def solution(a, b):
    return (dt.datetime(2016, a, b)).strftime("%a").upper()

a = 5
b = 24
print(solution(a, b))