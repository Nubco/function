#np.array() 핵심목적
# 파이썬 리스트를 NumPy 배열(ndarray)로 변환하여
# 수치 계산 및 벡터 연산이 가능하게 함

import numpy as np

lst = [1, 2, 3, 4]
arr = np.array(lst)

print(arr)        # [1 2 3 4]
print(type(arr))  # <class 'numpy.ndarray'>
