#include <bits/stdc++.h>

using namespace std;
int isVisited[100001];
bool done[100001];
int graph[100001];
int answer;

void dfs(int v, int cd)
{
	int next = graph[v];
	if (done[next] == true)
	{
		return;
	}

	if (isVisited[next] > 0 )
	{
		int loopCnt = cd - isVisited[next];
		answer += loopCnt;
	}

	else
	{
		if (isVisited[next] == 0) {
			isVisited[next] = cd;
			dfs(next, cd + 1);
			done[next] = true;
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	//freopen("input.txt", "r", stdin);
	int count;
	cin >> count;
	for (int i = 0; i < count; i++) {
		int cc;
		cin >> cc;
		for (int j = 1; j <= cc; j++) {
			cin >> graph[j];
		}

		std::fill(isVisited, isVisited + 100001, 0);
		std::fill(done, done + 100001, 0);

		for (int j = 1; j <= cc; j++) {
			dfs(j, 1);
		}
		
		cout << cc - answer << "\n";
		answer = 0;
	}

}