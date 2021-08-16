from sys import stdin, stdout

for _ in range(int(input())):
    word1, word2 = input().split()

    l1 = len(word1)
    l2 = len(word2)
    if l1 > l2:
        print("NO")
        continue
    if word1[0] != word2[0]:
        print("NO")
        continue
    i = j = 1
    # try:
    while( i < l1):
        if word1[i] == word2[j]:
            i += 1
            j += 1

        ## WALK ALONG THE LETTERS UNTIL A DIFFERENCE
        else:
            if word2[j] == word1[i -1]:
                for _ in word2[j:]:
                    if word2[j] != word1[i -1]: break
                    j += 1
                if j == l2: break

                    ## PASS OVER THE REPEATED LETTER
            else:
                break
    # except IndexError as e:
    #     print(e)
    #     print(str(i) + ", " + str(j) + word1 + word2)
    if i == l1:
        while(j < len(word2) and word2[j] == word1[-1]):
            j += 1
    result = "YES" if (i == len(word1)) and (j == len(word2)) else "NO"
    print(result)
