#include <bits/stdc++.h>

using namespace std;

int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, -1, 0, 1 };
int graph[126][126];
int isVisit[126][126];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	//freopen("input.txt", "r", stdin);
	int count = 0;
	int index = 1;
	while (1) {
		cin >> count;
		int v = 0;
		if (count == 0) break;
		for (int i = 0; i < count; i++) {
			for (int j = 0; j < count; j++) {
				cin >> v;
				graph[i][j] = v;
			}
			fill(isVisit[i], isVisit[i] + count, 0x3f3f3f3f);
		}

		priority_queue < tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
		pq.push({ graph[0][0], 0, 0 });
		isVisit[0][0] = graph[0][0];
		while (!pq.empty()) {
			int v, x, y;
			tie(v, x, y) = pq.top(); pq.pop();
			if (v != isVisit[x][y]) continue;
			for (int i = 0; i < 4; i++) {
				int cx = x + dx[i];
				int cy = y + dy[i];
				if (cx >= 0 && cy >= 0 && cx < count && cy < count) {
					int dist = v + graph[cx][cy];
					if (dist < isVisit[cx][cy]) {
						isVisit[cx][cy] = dist;
						pq.push({ isVisit[cx][cy] , cx, cy});
					}
				}
			}
		}

		cout << "Problem "<< index << ": " << isVisit[count - 1][count - 1] << "\n";
		index++;
	}
}