#min() 함수 핵심목적
# 여러 값 또는 iterable에서 가장 작은 값을 구하기 위해 사용


#기본 사용 (여러 값 비교)
a = 3
b = 7
c = 5

m = min(a, b, c)
print(m)          # 3


#기본 사용 (리스트)
nums = [1, 9, 3, 7, 2]
m = min(nums)
print(m)          # 1


#문자열 비교
# 아스키코드(사전순) 기준으로 가장 작은 값 반환
chars = ['a', 'z', 'b']
m = min(chars)
print(m)          # 'a'


#문자열 길이 기준 비교 (key 사용)
words = ["apple", "banana", "kiwi"]

m = min(words, key=len)
print(m)          # 'kiwi'



#algorithm (min 직접 구현)

# 목적:
# - min() 없이 최솟값 찾기
# - 반복문 기반 비교 알고리즘 이해

nums = [1, 9, 3, 7, 2]
m = nums[0]        # 첫 값을 기준값으로 설정

for n in nums:
    if n < m:
        m = n

print(m)           # 1



#algorithm (index까지 함께 찾기)

nums = [1, 9, 3, 7, 2]
m = nums[0]
idx = 0

for i in range(1, len(nums)):
    if nums[i] < m:
        m = nums[i]
        idx = i

print(m, idx)      # 1 0



#algorithm (2차원 리스트에서 최솟값)

matrix = [
    [1, 2, 3],
    [9, 4, 5],
    [6, 7, 8]
]

m = matrix[0][0]

for row in matrix:
    for val in row:
        if val < m:
            m = val

print(m)           # 1



#주의사항

# min()은 비어있는 iterable에 사용하면 에러 발생
# min([]) -> ValueError

# 해결 방법
nums = []
if nums:
    print(min(nums))
else:
    print("empty list")



#실전 포인트

# - 코딩 테스트에서는 min() 적극 사용
# - 조건 기준 비교는 key 활용
# - 알고리즘 문제에서는 직접 구현 요구 가능
