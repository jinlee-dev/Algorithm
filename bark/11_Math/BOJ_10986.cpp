#include <bits/stdc++.h>

using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	//freopen("input.txt", "r", stdin);

	int n, m;
	cin >> n >> m;
	long long sum = 0;
	long long value = 0;

	long long ret = 0;
	long long mod[1001];
	std::fill(mod, mod + 1001, 0);

	for (int i = 0; i < n; i++) {
		cin >> value;
		sum += value;
		mod[sum % m]++;

		if (sum % m == 0) {
			ret++;
		}

	}

	for (int i = 0; i <= m; i++) {
		ret += (mod[i] * (mod[i] - 1) / 2);
	}

	cout << ret;
}