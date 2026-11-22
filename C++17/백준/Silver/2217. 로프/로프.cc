# include <iostream>
# include <algorithm>
# include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, MAX = 0; // 1 <= N <= 100,000
    cin >> N;

    vector<int> rope(N, 0); // 1 <= rope[i] <= 10,000
    for (auto& x: rope)
        cin >> x;
    
    sort(rope.begin(), rope.end());
    for (int i=0; i < N; i++)
        MAX = max(MAX, rope[i] * (N-i));
    
    cout << MAX;
}


/*
N개의 로프가 있을때, 최대로 들 수 있는 무게


2
10
15

20
*/