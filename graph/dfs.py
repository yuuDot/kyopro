n = int(input())

vis = [False] * n
g = [[] for _ in range(n)]


def dfs(now, vis):
    for i in g[now]:
        if not vis[i]:
            vis[i] = True
            dfs(i, vis)

            vis[i] = False
