import fileinput
input1 = fileinput.input()

napps = int(input1.readline())
users = input1.readline()
users = users.rsplit()
users = [int(i) for i in users]
list.sort(users)
l = len(users)


if l == 0 or users[-1] == 0:
    print(0)

else:
    count = 1
    for i in range(l-1, -1, -1):
        if count > users[i]:
            break
        count += 1

    print(count-1)
