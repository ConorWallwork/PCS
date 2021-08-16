from sys import stdin, stdout
import math
nvenues, k = map(int, input().split())
maxi = -math.inf

for _ in range(nvenues):
    f, t = map(int, input().split())
    maxi = maxi if f <= maxi else (f if k >= t else max(maxi, f - (t - k)))


print(maxi)
