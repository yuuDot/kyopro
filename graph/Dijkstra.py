import heapq


def dijkstra(start_edge, goal_edge):  # 開始のi, j座標ゴール座標足してもいい
    que = [(0, start_edge)]
    # 条件つけて隣接を探索するなら
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 距離のリスト、適宜変更
    dist = [10**7] * n
    while que:
        now_cost, now_edge = heapq.heappop(que)
        if now_cost > dist[now_edge]:
            continue

        for nxt_edge, edge_cost in g[now_edge]:
            # コストの更新
            nxt_cost = now_cost + edge_cost
            if nxt_cost < dist[nxt_edge]:
                dist[nxt_edge] = nxt_cost
                heapq.heappush(que, (nxt_cost, nxt_edge))

    return dist[goal_edge]
