# サイクルを一つ検出したら、その辺番号を出力する
# Library Checker "Cycle Detection(Directed) 3114ms で通った"

import pypyjit
import sys

pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
edge_num = {}
for i in range(m):
    u, v = map(int, input().split())
    if (u, v) in edge_num:
        continue

    g[u].append(v)
    edge_num[(u, v)] = i

vis = [False] * n
checked = [False] * n
cycle = []


def dfs(crr: int, node: list, ans=[]) -> list:
    vis[crr] = True
    node.append(crr)
    for nxt in g[crr]:
        if not vis[nxt]:
            ans = dfs(nxt, node, ans)
            if len(ans) != 0:
                return ans
        elif not checked[nxt]:
            a = []
            cnt = -1
            while node[cnt] != nxt:
                a.append(node[cnt])
                cnt -= 1
            a.append(node[cnt])
            # cycle.append(tuple(a[::-1]))
            node.pop()
            checked[crr] = True
            return a[::-1]

    node.pop()
    checked[crr] = True

    return ans


for i in range(n):
    if not vis[i]:
        cycle = dfs(i, [])

    # print(cycle)
    if cycle:
        cycle.append(cycle[0])
        ans = []
        for i in range(len(cycle) - 1):
            ans.append(edge_num[(cycle[i], cycle[i + 1])])

        print(len(ans))
        print(*ans, sep="\n")
        exit()

print(-1)
