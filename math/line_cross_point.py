# https://tjkendev.github.io/procon-library/python/geometry/line_cross_point.html


def line_cross_point(P0, P1, Q0, Q1):
    """
    P0, P1 -> (a, b), (c, d)の形でこの二点を通る直線
    Q0, Q1も同じ
    P, Qであらわされる二直線の交点をfloatで返す
    """
    x0, y0 = P0
    x1, y1 = P1
    x2, y2 = Q0
    x3, y3 = Q1
    a0 = x1 - x0
    b0 = y1 - y0
    a2 = x3 - x2
    b2 = y3 - y2

    d = a0 * b2 - a2 * b0
    if d == 0:
        # two lines are parallel
        return None

    # s = sn/d
    sn = b2 * (x2 - x0) - a2 * (y2 - y0)
    # t = tn/d
    # tn = b0 * (x2-x0) - a0 * (y2-y0)
    return x0 + a0 * sn / d, y0 + b0 * sn / d
