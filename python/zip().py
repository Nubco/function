# zip() 핵심 목적
# 여러 iterable을 같은 위치(인덱스)끼리 묶어서 동시에 순회하고 싶을 때 사용


A = [1, 2, 3]
B = [4, 5, 6]

for a, b in zip(A, B):
    print(a, b)
# 1 4
# 2 5
# 3 6


# 실전 사용 (두 리스트 비교)
A = [1, 2, 3]
B = [1, 4, 3]

for a, b in zip(A, B):
    if a != b:
        print(a, b)


# algorithm (zip 없이 구현)
A = [1, 2, 3]
B = [4, 5, 6]

for i in range(len(A)):
    print(A[i], B[i])


# 내부 동작 느낌
def my_zip(a, b):
    n = min(len(a), len(b))
    for i in range(n):
        yield a[i], b[i]


#for i in range(len())가 보이면 enumerate나 zip으로 바꿀 수 있는지 먼저 생각한다.