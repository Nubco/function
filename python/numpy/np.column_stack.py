#np.column_stack() 핵심목적
# 여러 1차원 배열을 열(column) 기준으로 결합

import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

z = np.column_stack((x, y))

print(z)
# [[1 4]
#  [2 5]
#  [3 6]]
