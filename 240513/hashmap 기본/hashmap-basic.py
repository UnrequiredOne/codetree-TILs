n = int(input())
arr = {}
for i in range(n):
    cmd = list(input().split())
    if cmd[0] == "add":
        arr[cmd[1]] = cmd[2]
    elif cmd[0] == "remove":
        arr.pop(cmd[1])
    elif cmd[0] == "find":
        if cmd[1] not in arr:
            print("None")
        else:
            print(arr[cmd[1]])