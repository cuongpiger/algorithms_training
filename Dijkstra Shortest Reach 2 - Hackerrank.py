'''
https://www.hackerrank.com/challenges/dijkstrashortreach/problem
Comment
This is accepted code, but it will be running time error, have to convert this code to C++ to get AC
'''
import sys
import queue

def FILE_IO():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

'''____________________________________________________________________________________________'''

INF = 10**9
grp = [[] for i in range(3005)]
n = s = None

def dijkstra():
    dist = [INF]*(n + 5)
    dist[s] = 0
    pq = queue.PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        wu, u = pq.get()

        if wu != dist[u]:
            continue

        for v, wv in grp[u]:
            if dist[v] > wv + wu:
                dist[v] = wv + wu;
                pq.put((dist[v], v))

    return dist

#_____main_____
#FILE_IO()

tc = int(input())

for cs in range(tc):
    n, m = map(int, input().split())
    for i in range(m):
        u, v, w = map(int, input().split())
        grp[u].append((v, w))
        grp[v].append((u, w))

    s = int(input())
    dist = dijkstra()

    for i in range(1, n + 1):
        grp[i].clear()
        if i == s:
            continue

        if dist[i] == INF:
            print(-1, end = ' ')
        else:
            print(dist[i], end = ' ')
    
    print()


