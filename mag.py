import fileinput
input1 = fileinput.input()

word1 = input1.readline().rstrip()
word2 = input1.readline().rstrip()


count1 = [0 for i in range(27)]
count2 = [0 for i in range(27)]


def getIndex(c):
    if(c == ' '): return 26
    return ord(c) - ord('a')


n = max(len(word1), len(word2))

for i in range(0,n):
    if(i < len(word1)):

        index1 = getIndex(word1[i])
        count1[index1] += 1
    if(i < len(word2)):
        index2 = getIndex(word2[i])
        count2[index2] += 1

diff = 0
for i in range(0,27):
    diff += abs(count1[i] - count2[i])

print(diff)
