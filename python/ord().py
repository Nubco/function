#ord()핵심목적
#문자 하나를 아스키 코드 값(정수)으로 변환하고 싶을 때 사용
print(ord('a'))  # 97
print(ord('A'))  # 65
print(ord('0'))  # 48


text = "abc"
ascii_codes = list(map(ord, text))
print(ascii_codes)  # [97, 98, 99]

digits = "123"
numbers = [ord(ch) - ord('0') for ch in digits]
print(numbers)  # [1, 2, 3]

#algorithm
def my_ord(ch):
    ascii_table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return ascii_table.index(ch)   # 단순 예시

print(my_ord('A'))  # 10 (실제 ord는 65)
