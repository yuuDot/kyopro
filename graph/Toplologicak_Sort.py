import heapq

n, m = map(int, input().split())
deg_in = [0] * n
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    deg_in[v] += 1

# トポロジカルソートされたもののうち、辞書順で一番早いもの
# 特に必要ないなら普通のキューでいい
hq = [i for i in range(n) if deg_in[i] == 0]
result = []
heapq.heapify(hq)
while hq:
    q = heapq.heappop()
    result.append(q)
    for i in g[q]:
        deg_in[i] -= 1
        if deg_in[i] == 0:
            heapq.heappush(hq, i)

# DAGでなければこれに引っかかる
assert len(result) == n, "This graph is not DAG"
