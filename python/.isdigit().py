# .isdigit() 핵심 목적
# 문자가 숫자인지 판별하고 싶을 때


print("123".isdigit())   # True
print("12a".isdigit())   # False


# algorithm
def my_isdigit(s):
    for ch in s:
        if ch < '0' or ch > '9':
            return False
    return True
