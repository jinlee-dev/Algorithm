import sys

l = list(str(sys.stdin.readline().rstrip()))
cal = []

number = ""
tempNumber = 0
for i in l:
    if i != '+' and i != '-':
        number = number + i
    else:
        if i == '-':
            cal.append(tempNumber + int(number))
            tempNumber = 0
        else:
            tempNumber = tempNumber + int(number)
        number = ""
        
tempNumber = int(number) + tempNumber

cal.append(tempNumber)
answer = cal[0]
for i in range(1, len(cal)):
    answer = answer - cal[i]

print(answer)