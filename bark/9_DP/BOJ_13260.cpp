#include <bits/stdc++.h>

using namespace std;

int dp[1001][1001];
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	//freopen("input.txt", "r", stdin);
	
	int answer = 0;
	int size, count, idx;
	cin >> size >> count;
	vector<int> accSum;
	for (int i = 0; i < count; i++) {
		cin >> idx;
		accSum.push_back(idx);
	}
	accSum.push_back(size);

	sort(accSum.begin(), accSum.end());
	
	int cutSize = accSum.size();
	for (int i = 0; i < cutSize; i++) {
		fill(dp[i], dp[i] + 1001, 0x3f3f3f3f);
		dp[i][i] = 0;
	}

	// 차이가 얼마나 나느냐까지
	for (int diff = 1; diff <= cutSize; diff++) {
		// 돌릴 횟수
		// 3번, 2번, 1번
		for (int st = 0; st < cutSize - diff; st++) {
			int et = st + diff;
			int sum = (st - 1 < 0 ) ? accSum[et] : accSum[et] - accSum[st - 1];
			for (int k = st; k < et; k++) {
				// 점화식 : dp[0][3] = (dp[0][0] + dp[1][3], dp[0][1] + dp[2][3], dp[0][2] + dp[3][3]) + sum
				// 이런데서 만들면 버그 생긴다
				// 예외 케이스가 있는지 확인을 해봐야 함
				// 점화식 이해하기 -> 복습
				dp[st][et] = std::min(dp[st][k] + dp[k + 1][et] + sum, dp[st][et]);
			}
		}
	}
	cout << dp[0][cutSize - 1];
}