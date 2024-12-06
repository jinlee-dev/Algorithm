import sys

pokemonCnt, problemCnt = map(int, sys.stdin.readline().split(" "))

dicNum = {}
dicMonster= {}
for i in range(pokemonCnt):
    dicNum[i + 1] = str(sys.stdin.readline().rstrip())
    dicMonster[dicNum[i + 1]] = i + 1

for i in range(problemCnt):
    problem = str(sys.stdin.readline().rstrip())
    if True == problem.isdigit():
        print(dicNum[int(problem)])
    else:
        print(dicMonster[problem])