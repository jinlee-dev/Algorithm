#include <bits/stdc++.h>

using namespace std;

long long accSize[1'000'001];
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("input.txt", "r", stdin);
	
	vector<pair<long long, long long>> line;
	long long lineCnt, goal;
	cin >> lineCnt >> goal;
	long long s, e;
	for (int i = 0; i < lineCnt; i++) {
		cin >> s >> e;
		line.push_back({ s, e });
	}
	
	sort(line.begin(), line.end());

	long long sp, ep;
	int minVal = line[0].first;
	int maxVal = line[0].first;
	for (auto& it : line) {

		for (int i = it.first + 1; i <= it.second; i++) {
			accSize[i]++;
			minVal = min(i, minVal);
			maxVal = max(i, maxVal);
		}
	}


	for (int i = 0; i <= maxVal; i++) {
		accSize[i + 1] += accSize[i];
	}


	sp = 0; ep = 1;
	while (sp <= ep) {
		long long length = 0;
		
		if (ep > 1'000'000 || sp < 0) {
			break;
		}

		length = (long long)accSize[ep] - (long long)accSize[sp];
	
		if (length ==  goal) {
			cout << sp << " " << ep;
			return 0;
		}
		else if (length < goal) {
			ep++;
		}
		else
		{
			sp++;
		}
	}

	cout << "0 0";
}