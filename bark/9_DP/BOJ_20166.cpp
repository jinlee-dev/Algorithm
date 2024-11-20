#include <bits/stdc++.h>

using namespace std;

int dx[] = { -1, -1, -1, 0, 0, 1, 1, 1 };
int dy[] = { -1, 0, 1, -1, 1, -1, 0, 1 };
char graph[11][11];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	//freopen("input.txt", "r", stdin);
	int n, m, k;
	cin >> n >> m >> k;
	for (int i = 0; i < n; i++) {
		std::string str;
		cin >> str;
		for (int j = 0; j < m; j++) {
			graph[i][j] = str[j];
		}
	}

	for (int i = 0; i < k; i++) {
		std::string str;
		cin >> str;
		int dp[11][11][5];

		// dp값 초기화
		for (int j = 0; j < n; j++) {
			for (int t = 0; t < m; t++) {
				for (int dep = 0; dep < str.size(); dep++) {
					if (dep == 0)
					{
						string curStr;
						if (graph[j][t] == str[0]) {
							dp[j][t][dep] = 1;
						}
						else {
							dp[j][t][dep] = 0;
						}
					}
					else {
						dp[j][t][dep] = 0;
					}
				}
			}
		}


		for (int dep = 1; dep < str.size(); dep++) {
			for (int j = 0; j < n; j++) {
				for (int t = 0; t < m; t++) {
					for (int p = 0; p < 8; p++) {
						int cx = j + dx[p];
						int cy = t + dy[p];

						if (cx >= n) {
							cx = 0;
						}
						else if (cx < 0) {
							cx = n - 1;
						}

						if (cy >= m) {
							cy = 0;
						}
						else if (cy < 0) {
							cy = m - 1;
						}

						if (graph[cx][cy] == str[dep]) {
							dp[cx][cy][dep] += dp[j][t][dep - 1];
						}
					}
				}
			}
		}

		int answer = 0;

		for (int j = 0; j < n; j++) {
			for (int t = 0; t < m; t++) {
				answer += dp[j][t][str.size() - 1];
			}
		}
		
		cout << answer;
		if (i < k - 1) {
			cout << '\n';
		}
	}
}