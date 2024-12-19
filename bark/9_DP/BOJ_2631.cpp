
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int dp[201];
int row[201];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int count;
	int answer = 0;
	cin >> count;
	for (int i = 1; i <= count; i++)
	{
		cin >> row[i];
	}

	dp[1] = 1;
	for (int i = 2; i <= count; i++)
	{
		dp[i] = 1;
		for (int j = i - 1; j > 0; j--)
		{
			if (row[j] < row[i])
			{
				dp[i] = max(dp[i], dp[j] + 1);
				answer = max(answer, dp[i]);
			}
		}
	}

	cout << count - answer;
	
}