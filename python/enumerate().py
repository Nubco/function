# enumerate() 핵심 목적
# 반복 가능한 객체를 순회하면서 (인덱스, 값)을 동시에 얻고 싶을 때 사용


nums = [10, 20, 30]

for i, v in enumerate(nums):
    print(i, v)
# 0 10
# 1 20
# 2 30

# 실전 사용 (인덱스 + 값 필요할 때)
nums = [5, 3, 8]

for i, v in enumerate(nums):
    if v > 5:
        print(i)


# algorithm (enumerate 없이 구현)
nums = [10, 20, 30]

for i in range(len(nums)):
    print(i, nums[i])


# 내부 동작 느낌
def my_enumerate(iterable):
    idx = 0
    for item in iterable:
        yield idx, item
        idx += 1

#for i in range(len())가 보이면 enumerate나 zip으로 바꿀 수 있는지 먼저 생각한다.