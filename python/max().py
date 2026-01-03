#max() 함수 핵심목적
# 여러 값 또는 iterable에서 가장 큰 값을 구하기 위해 사용


#기본 사용 (여러 값 비교)
a = 3
b = 7
c = 5

m = max(a, b, c)
print(m)          # 7


#기본 사용 (리스트)
nums = [1, 9, 3, 7, 2]
m = max(nums)
print(m)          # 9


#문자열 비교
# 아스키코드(사전순) 기준으로 가장 큰 값 반환
chars = ['a', 'z', 'b']
m = max(chars)
print(m)          # 'z'


#문자열 길이 기준 비교 (key 사용)
words = ["apple", "banana", "kiwi"]

m = max(words, key=len)
print(m)          # 'banana'



#algorithm (max 직접 구현)

# 목적:
# - max() 없이 최댓값 찾기
# - 반복문 기반 비교 알고리즘 이해

nums = [1, 9, 3, 7, 2]
m = nums[0]        # 첫 값을 기준값으로 설정

for n in nums:
    if n > m:
        m = n

print(m)           # 9



#algorithm (index까지 함께 찾기)

nums = [1, 9, 3, 7, 2]
m = nums[0]
idx = 0

for i in range(1, len(nums)):
    if nums[i] > m:
        m = nums[i]
        idx = i

print(m, idx)      # 9 1



#algorithm (2차원 리스트에서 최대값)

matrix = [
    [1, 2, 3],
    [9, 4, 5],
    [6, 7, 8]
]

m = matrix[0][0]

for row in matrix:
    for val in row:
        if val > m:
            m = val

print(m)           # 9



#주의사항

# max()는 비어있는 iterable에 사용하면 에러 발생
# max([]) -> ValueError

# 해결 방법
nums = []
if nums:
    print(max(nums))
else:
    print("empty list")



#실전 포인트

#  코딩 테스트에서는 max() 적극 사용
#  조건 기준 비교는 key 활용
#  알고리즘 문제에서는 직접 구현 요구 가능
