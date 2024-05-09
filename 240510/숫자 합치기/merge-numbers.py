n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

answer = 0
while len(arr) > 1:
    tmp = arr.pop() + arr.pop()
    answer += tmp
    arr.append(tmp)
    arr.sort(reverse=True)

print(answer)