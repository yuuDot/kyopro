from atcoder.segtree import SegTree


# 区間に対する演算maxとかminとか
def op(a, b):
    return max(a, b)


# op(a, e) = a
e = 0

n = int(input())
# SegTree(op, e, n) -> nがintなら要素数nのsegtreeが、listならそれを載せてsegtreeができる
tree = SegTree(op, e, n)
