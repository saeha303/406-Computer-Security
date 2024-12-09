import time
import _1905033_utils_elliptic

timeA = 0
timeB = 0
timeR = 0
print('Computation time for-')
for i in range(3):
    if i ==0:
        intended_len = 128
    elif i ==1:
        intended_len = 192
    else:
        intended_len = 256
    print('k: ',intended_len)
    p, ka, kb, a, b, x1, y1 = _1905033_utils_elliptic.generate(intended_len)
    for j in range(5):
        start_time = time.time()
        Ax, Ay = _1905033_utils_elliptic.calculateAB(ka, a, b, p, x1, y1)

        timeA += time.time() - start_time
        start_time = time.time()
        Bx, By = _1905033_utils_elliptic.calculateAB(kb, a, b, p, x1, y1)

        timeB += time.time() - start_time
        start_time = time.time()
        sx, sy = _1905033_utils_elliptic.calculateAB(ka, a, b, p, Bx, By)
        # print(sx,sy)
        timeR += time.time() - start_time
        sx, sy = _1905033_utils_elliptic.calculateAB(kb, a, b, p, Ax, Ay)
        # print(sx,sy)
    print('A: ',timeA*1000 / 5,' msec')
    print('B: ',timeB*1000 / 5,' msec')
    print('shared key R: ',timeR*1000 / 5,' msec')
