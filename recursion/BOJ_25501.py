global count
count = 1

def recursion(s, l, r):
    global count
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        count = count + 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)

x = int(input())
inputCnt = 0
strList = list()
while inputCnt < x:
     strList.append(input())
     inputCnt = inputCnt + 1

for str in strList:
    isPd = isPalindrome(str)
    print('{0} {1}'.format(isPd, count))
    count = 1
    