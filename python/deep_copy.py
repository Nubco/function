#깊은 복사(Deep Copy) 핵심목적
# 객체와 내부 데이터까지 모두 새로 복사하여
# 원본과 완전히 독립적인 구조를 만들기 위함


#기본 예제 (중첩 리스트)
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)    # 깊은 복사

b[0][0] = 99

print(a)                # [[1, 2], [3, 4]]
print(b)                # [[99, 2], [3, 4]]


#얕은 복사와 차이 확인
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

print(a is b)           # False (겉껍질 다름)
print(a[0] is b[0])     # False (내부도 다름)



#algorithm (구조 전체 독립성 확인)

# 내부 요소의 주소까지 완전히 다름
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

for i in range(len(a)):
    print(a[i] is b[i]) # 모두 False



#딕셔너리 예제
a = {
    "layers": [64, 128, 256],
    "config": {"lr": 0.001}
}

b = copy.deepcopy(a)

b["layers"].append(512)
b["config"]["lr"] = 0.01

print(a)  # {'layers': [64, 128, 256], 'config': {'lr': 0.001}}
print(b)  # {'layers': [64, 128, 256, 512], 'config': {'lr': 0.01}



#직접 구현 예제 (2차원 리스트 깊은 복사)

a = [[1, 2], [3, 4]]
b = []

for row in a:
    b.append(row[:])    # 각 행을 새로 복사

b[1][0] = 99

print(a)                # [[1, 2], [3, 4]]
print(b)                # [[1, 2], [99, 4]]



#주의사항

# deepcopy는 안전하지만
# - 속도가 느릴 수 있음
# - 메모리 사용량 증가
# - 매우 큰 객체에서는 성능 이슈 발생 가능



#사용 기준

# - 상태(State)를 보호해야 할 때
# - 설정값, 모델 파라미터, 학습 데이터
# - 함수 인자로 객체를 넘길 때
# - 원본 오염이 치명적인 경우
