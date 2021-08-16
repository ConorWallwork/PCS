from sys import stdin, stdout

for _ in range(int(input())):
    word1, word2 = input().split()

    len1 = len(word1)
    len2 = len(word2)

    if word1[-len1] != word2[-len2]:
        print("NO")
        continue

    while(len2 >= len1 and len1 != 0):
        if word2[-len2] == word1[-len1]:
            len2 -= 1
            len1 -= 1
        else:
            if word1[-(len1 + 1)] == word2[-len2]:
                len2 -= 1
            else:
                break

    if len2 < len1 or len1 != 0:
        print("NO")
        continue

    while(len2 > 0 and word2[-len2] == word1[-1]):
        len2 -= 1

    print("YES" if len2 == 0 else "NO")
