#include <bits/stdc++.h>

using namespace std;

int city[101];
int isVisit[101];
vector <pair<int, int>> graph[101];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	//freopen("input.txt", "r", stdin);
	int cityCnt, dist, edge, d;
	cin >> cityCnt >> dist >> edge;
	for (int i = 1; i <= cityCnt; i++) {
		cin >> d;
		city[i] = d;
	}

	int s, e, v;
	for (int i = 0; i < edge; i++) {
		cin >> s >> e >> v;
		graph[s].push_back({ v, e });
		graph[e].push_back({ v, s });
	}

	int answer = 0;
	for (int i = 1; i <= cityCnt; i++) {
		fill(isVisit, isVisit + cityCnt + 1, 999);
		priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
		pq.push({ 0,i });
		isVisit[i] = 0;

		while (!pq.empty()) {
			int dist, e;
			tie(dist, e) = pq.top(); pq.pop();
			if (dist != isVisit[e]) continue;
			for (auto& it : graph[e]) {

				int curDist = dist + it.first;

				if (curDist < isVisit[it.second]) {

					isVisit[it.second] = curDist;
					pq.push({ curDist, it.second });
				}
			}
		}

		int curAnswer = 0;
		for (int j = 1; j <= cityCnt; j++) {
			if (isVisit[j] <= dist) {
				curAnswer += city[j];
			}
		}

		answer = max(answer, curAnswer);
	}

	cout << answer;

}