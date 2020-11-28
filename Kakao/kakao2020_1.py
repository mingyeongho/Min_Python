import re
def solution(s) :
    for i in range(1, len(s) // 2 + 1) :
        reList = re.sub('(\w{%i})' %i, '\g<i> ', s).split()
        print(reList)