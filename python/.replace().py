# .replace() 핵심 목적
# 문자열 일부를 다른 문자열로 치환하고 싶을 때


text = "a-b-c"
print(text.replace("-", ","))   # "a,b,c"


# algorithm
result = ""
for ch in text:
    if ch == "-":
        result += ","
    else:
        result += ch
