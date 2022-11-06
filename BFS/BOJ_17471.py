import sys
from itertools import combinations
from collections import deque

def IsConnected(graph, s):
    if len(s) == 1:
        return True

    count = 1
    sLen = len(graph)
    
    graphList = [False for row in range(sLen + 1)]
    for i in s:
        graphList[i] = True
        
    isVisited = [False for row in range(sLen + 1)]
    q = deque()
    q.append(s[0])
    isVisited[s[0]] = True

    while len(q):
        v = q.popleft()
        for i in graph[v]:
            if isVisited[i] == False and graphList[i] == True:
                isVisited[i] = True
                q.append(i)
                count = count + 1

    return count == len(s)
            
def GetPopulation(c, p):
    population = 0
    for i in c:
        population = population + p[i]
    return population



count = int(sys.stdin.readline())
population = [0]

inputPop = map(int, sys.stdin.readline().split(" "))
geri = []

index = 1
for i in inputPop:
    population.append(i)
    geri.append(index)
    index = index + 1

graph = [[] for row in range(count + 1)]
linkList = []
for i in range(count):
    linkList.append(list(map(int, sys.stdin.readline().split(" "))))

populationDiff = int(1e9)

index = 1
for i in linkList:
    connectedLinkCnt = i[0]
    for j in range(connectedLinkCnt):
        graph[index].append(i[j + 1])
    index = index + 1

for i in range(1, count):
    combiList = list(combinations(geri, i))
    for j in combiList:
        # 조합으로 선정된 선거구
        s1 = list(j)
        # 조합으로 선정된 선거구를 제외한 선거구
        s2 = list(geri)
        for k in j:
            s2.remove(k)
        # 두 선거구의 연결 유무를 구한다
        if IsConnected(graph, s1) and IsConnected(graph, s2):
            #연결되어 있으면 두 선거구의 인원을 구한다
            s1Population = GetPopulation(s1, population)
            s2Population = GetPopulation(s2, population)
            populationDiff = min(abs(s2Population - s1Population), populationDiff)

if populationDiff == int(1e9):
    print(-1)
else:
    print(populationDiff)