# 핵심 목적
# 문자열이 특정 패턴으로 시작/끝나는지 확인

text = "hello.py"
print(text.endswith(".py"))     # True
print(text.startswith("he"))    # True

# algorithm
def starts_with(s, prefix):
    return s[:len(prefix)] == prefix
