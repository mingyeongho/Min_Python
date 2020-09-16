#이차원 리스트
words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)

stuff = [[w.upper(), w.lower(), len(w)]for w in words]
for i in stuff :
    print(i)

case_1 = ['A', 'B', 'C']
case_2 = ['D', 'E', 'A']
result = [[i+j for i in case_1] for j in case_2] # 뒤에 for문이 먼저 실행
print(result)