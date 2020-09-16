word_1 = 'hello'
word_2 = 'world'
result = [i + j for i in word_1 for j in word_2]
print(result)

# 중첩 반복문에도 필터링 가능
case_1 = ['A', 'B', 'C']
case_2 = ['D', 'E', 'A']
result = [i+j for i in case_1 for j in case_2 if not(i==j)]
print(result)