import sys

s1 = list()
l = list(map(str, sys.stdin.readline().rstrip()))
for i in range(len(l)):
    if len(s1) == 0 or l[i] == '(' or l[i] == '[':
        s1.append(l[i])
    else:
        if len(s1) == 0:
            s1.clear()
            break
        else:
            # 숫자일경우
            if l[i] == ')' and l[i - 1] == '(':
                s1.pop()
                s1.append(2)
            elif l[i] == ']' and l[i - 1] == '[':
                s1.pop()
                s1.append(3)
            # 문자일 경우
            else:
                # 다음 괄호가 나올 때까지 돌린다
                t = s1.pop()
                tmpRet = 0
                while t != '[' and t != '(' and len(s1) != 0:
                    tmpRet = tmpRet + t
                    t = s1.pop()
                # 괄호짝이 맞을 경우 계산해준다
                if t == '(' and l[i] == ')':
                    s1.append(tmpRet * 2)
                elif t == '[' and l[i] == ']':
                    s1.append(tmpRet * 3)
                else:
                    s1.clear()
                    break

retVal = 0

for i in s1:
    if False == str(i).isdigit() :
        retVal = 0
        break
    else:
        retVal = i + retVal

print(retVal)

                 


