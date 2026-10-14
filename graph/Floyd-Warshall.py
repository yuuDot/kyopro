n, m = map(int, input().split())
INF = 1 << 60
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
for _ in range(m):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    dist[u][v] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
