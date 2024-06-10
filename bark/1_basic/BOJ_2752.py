import sys
s = list(map(int, input().split()))
s.sort()
print("%d %d %d" % (s[0],s[1] , s[2]))