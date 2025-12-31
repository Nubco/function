#얕은 복사(Shallow Copy) 핵심목적
# 객체 자체는 새로 만들되, 내부 데이터(참조)는 원본과 공유


#기본 예제 (리스트)
a = [1, 2, 3]
b = a[:]          # 얕은 복사
b[0] = 99

print(a)          # [1, 2, 3]
print(b)          # [99, 2, 3]


#중첩 리스트 예제 (얕은 복사의 핵심)
a = [[1, 2], [3, 4]]
b = a[:]          # 얕은 복사

b[0][0] = 99

print(a)          # [[99, 2], [3, 4]]
print(b)          # [[99, 2], [3, 4]]



#algorithm (참조 구조 확인)

# a와 b는 다른 리스트지만
# 내부 요소는 같은 주소를 참조
a = [[1, 2], [3, 4]]
b = a[:]

print(a is b)         # False (겉껍질은 다름)
print(a[0] is b[0])   # True  (내부는 공유)



#copy 모듈 사용
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)      # 얕은 복사

b[1][1] = 99

print(a)              # [[1, 2], [3, 99]]
print(b)              # [[1, 2], [3, 99]]



#얕은 복사가 발생하는 경우

a = [1, 2, 3]
b = list(a)           # 얕은 복사

c = a.copy()          # 얕은 복사

d = a[:]              # 얕은 복사



#주의사항

# 얕은 복사는 내부 데이터 변경 시
# 원본 데이터가 함께 변경될 수 있음

config = {
    "layers": [64, 128, 256]
}

backup = config.copy()    # 얕은 복사
backup["layers"].append(512)

print(config["layers"])   # [64, 128, 256, 512]
