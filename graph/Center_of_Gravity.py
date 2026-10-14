import sys

sys.setrecursionlimit(10**7)

n = 10**5
weight = [0] * n
centroid = []
g = [[] for _ in range(n)]


def find_center_of_gravity(now, before):
    weight[now] = 1  # 基本は辺の数。重みが付いていたら変更
    mx = 0
    for i in g[now]:
        if i == before:
            continue
        weight[now] += find_center_of_gravity(i, now)
        mx = max(mx, weight[i])  # 最大の子の部分木のサイズ

    mx = max(mx, n - weight[now])  # 親方向(子ではないほう)の部分木のサイズ
    if mx * 2 <= n:
        centroid.append(now)

    return weight[now]
