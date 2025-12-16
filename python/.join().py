# .join() 핵심 목적
# 문자열 리스트를 하나의 문자열로 합치고 싶을 때 사용

words = ["hello", "world"]
sentence = " ".join(words)
print(sentence)   # "hello world"


# algorithm
words = ["hello", "world"]
result = words[0]

for i in range(1, len(words)):
    result += " " + words[i]

print(result)
