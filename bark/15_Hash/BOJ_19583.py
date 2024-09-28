import sys
from datetime import datetime

start, end, stream = map(str, sys.stdin.readline().rstrip().split(" "))

start = 60*int(start[:2]) + int(start[3:])
end = 60*int(end[:2]) + int(end[3:])
stream = 60*int(stream[:2]) + int(stream[3:])
att = set()
cnt = 0
while 1:
	try:
		time, user = sys.stdin.readline().split()
		time = 60*int(time[:2]) + int(time[3:])
		if time <= start:
			att.add(user)
		elif time >= end and time <= stream:
			if user in att:
				cnt += 1
				att.remove(user)
		
	except:
		break

print(cnt)