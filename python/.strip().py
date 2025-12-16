# .strip() 핵심 목적
# 문자열 양쪽(앞뒤)의 공백이나 특정 문자를 제거하고 싶을 때


text = "   hello   "
print(text.strip())    # "hello"
print(text.lstrip())   # "hello   " l(eft)strip
print(text.rstrip())   # "   hello" r(ight)strip


# algorithm (개념)
while text and text[0] == " ":
    text = text[1:]

while text and text[-1] == " ":
    text = text[:-1]
