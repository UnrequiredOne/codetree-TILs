arr = list(map(int, input().split()))

answer = 0

if arr[2] - arr[1] > 2 and arr[1] - arr[0] > 2:
    answer = 2
elif arr[2] - arr[1] <= 1 and arr[1] - arr[0] <= 1:
    answer = 0
elif arr[2] - arr[1] <= 1 or arr[1] - arr[0] <= 1:
    answer = 2
else:
    answer = 1

print(answer)