#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int count = 0;
    cin >> count;
    vector<int> good;
    for (int i = 0; i < count; i++) {
        int v = 0;
        cin >> v;
        good.push_back(v);
    }
    sort(good.begin(), good.end());
    int answer = 0;
    for (int i = 0; i < count; i++) {
        int p0 = 0;
        int p1 = count - 1;

        while (true) {

            if (p0 < 0 || p1 < 0) {
                break;
            }

            if (p0 == p1) {
                break;
            }

            if (p0 == i) {
                p0++;
            }
            else if (p1 == i) {
                p1--;
            }


            else if (good[p0] + good[p1] == good[i]) {
                answer++;
                break;
            }
            else if (good[p0] + good[p1] < good[i]) {
                p0++;
            }
            else if (good[p0] + good[p1] > good[i]) {
                p1--;
            }
        }
    }
    cout << answer;
}