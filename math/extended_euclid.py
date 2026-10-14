def extended_euclid(a: int, b: int):
    """
    ax * by == 1となるx, yを返す。計算量log min(a, b)
    a, bは互いに素であることが要求される。
    答えが1以外であるときはa, bを何倍かする。
    """
    if b == 0:
        return (1, 0)
    xd, yd = extended_euclid(b, a % b)
    return (yd, xd - a // b * yd)
