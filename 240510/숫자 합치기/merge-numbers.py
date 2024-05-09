import heapq

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
while len(arr) > 1:
    a, b = heapq.heappop(arr), heapq.heappop(arr)
    answer += a + b
    heapq.heappush(arr, a+b)

print(answer)