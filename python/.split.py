#.split() 핵심목적
# 긴 문자열을 특정 구별자(공백, 쉼표 등) 기준으로 나누고 싶을 때 사용


line = "0 12 7"
parts = line.split()  # 공백 기준
print(parts)          # ['0', '12', '7']

text = "apple,banana,orange"
fruits = text.split(",") #쉼표 기준
print(fruits)  # ['apple', 'banana', 'orange']

line = "0 12 7"
nums = list(map(int, line.split()))
print(nums)  # [0, 12, 7]



#algorithm (숫자로 저장)

#split(구별자) → 구별자 기준으로 문자열 나눔
line = "0 12 7"
nums = []       # 결과 저장
num = 0         # 현재 숫자 누적
has_num = False # 숫자를 읽고 있는 중인지 표시

for ch in line + ' ':  # 마지막 숫자 처리 위해 공백 추가
    if '0' <= ch <= '9':          # 숫자라면
        num = num * 10 + (ord(ch) - ord('0'))  # 문자 → 숫자 누적
        has_num = True
    else:                         # 공백 또는 기타 문자
        if has_num:               # 이전에 숫자 읽었으면
            nums.append(num)      # 리스트에 저장
            num = 0
            has_num = False

print(nums)  # [0, 12, 7]



#algorithm (문자열로 저장)
line = "0 12 7"
nums = []
num = ""
for ch in line + " ":
    if ch != " ":
        num += ch
    else:
        if num:
            nums.append(num)
            num = ""

print(nums)  # ['0','12','7']

