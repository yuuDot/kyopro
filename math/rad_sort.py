# 早いが正確じゃないかも
import math

PI = math.pi
TWO_PI = PI * 2
deg = []
x1, y1 = 0, 0
for x2, y2 in xy:
    if x1 == x2 and y1 == y2:
        continue
    angle = math.atan2(y2 - y1, x2 - x1)
    if angle < 0:
        angle += TWO_PI
    deg.append(angle)
# 終わり


from functools import cmp_to_key


def arg_sort_cp(points, origin):
    x, y = origin

    def half(p):
        dx = p[0] - x
        dy = p[1] - y
        return 0 if (dy > 0 or (dy == 0 and dx >= 0)) else 1

    def cmp(a, b):
        ax, ay = a[0] - x, a[1] - y
        bx, by = b[0] - x, b[1] - y

        ha = half(a)
        hb = half(b)
        if ha != hb:
            return ha - hb

        cross = ax * by - ay * bx
        if cross > 0:
            return -1
        if cross < 0:
            return 1

        # 同じ方向なら距離で並べる
        da = ax * ax + ay * ay
        db = bx * bx + by * by
        return (da > db) - (da < db)

    return sorted(points, key=cmp_to_key(cmp))
