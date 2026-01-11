#np.random.shuffle() 핵심목적
# 배열의 순서를 무작위로 섞음
# 원본 배열을 직접 변경(in-place)

import numpy as np

a = np.arange(10)
np.random.shuffle(a)

print(a)  # 순서가 무작위로 섞인 배열
