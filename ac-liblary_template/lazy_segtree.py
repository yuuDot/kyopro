INF = 1 << 60
# mapping(data, ID) = data
ID = INF
ID = 0


# prodする計算
# ノードの型は (sum, length)
def op(x, y):
    # x, y: (sum, length)
    return (x[0] + y[0], x[1] + y[1])


# 単位元：和 が 0、長さは 0
# op(e, a) = a
def e():
    return (0, 0)


# 作用させたfをノードであるxに乗せる
# f: 代入値、 x: (sum, length)
# 区間変更 or add、区間max, minの時は長さの情報がいらない
def mapping_ch(f, x):
    if f == ID:
        return x
    _, length = x
    return (f * length, length)


def mapping_add(f, x):
    if f == ID:
        return x
    s, length = x
    return (f * length + s, length)


# 関数 f の合成
def composition_ch(f_new, f_old):
    return f_old if f_new == ID else f_new


def composition_add(f_new, f_old):
    if f_new == ID:
        return f_old
    return f_new + f_old


# mapping(ID, a) = a
def id_():
    return ID
