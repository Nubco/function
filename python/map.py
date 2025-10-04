# map()의 핵심 목적
#리스트나 문자열 등의 각 요소에 같은 작업을 반복적으로 적용하고 싶을 때 사용


line = "0 12 7".split()   # ['0', '12', '7']
numbers = list(map(int, line))  # [0, 12, 7]

text = "abc"
ascii_codes = list(map(ord, text))  # [97, 98, 99]

def square(x):
    return x*x

nums = [1,2,3,4]
squares = list(map(square, nums))  # [1,4,9,16]



#algorithm
digits = "123"  
numbers = []

for ch in digits:
    numbers.append(ord(ch) - ord('0'))
print(numbers)  # [1, 2, 3]


def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))  # 함수 적용
    return result

nums_str = ['1', '2', '3']
nums_int = my_map(int, nums_str)
print(list(nums_int))  # [1, 2, 3]