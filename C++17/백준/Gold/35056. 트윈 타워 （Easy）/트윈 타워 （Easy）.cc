# include <iostream>
# include <vector>
# include <algorithm>

using namespace std;
using ll = long long;

void solve(int N, vector<ll>& A, vector<ll>& B){
    vector<vector<ll>> DP(N, vector<ll>(N, 0));
    DP[0][0] = A[0];
    for (int i=1; i<N; i++)
        DP[i][0] = max(DP[i-1][0], A[i]);
    
    for (int i=1; i<N; i++){
        for (int j=1; j<i+1; j++){
            ll base = (i >= 2 && j >= 2) ? DP[i-2][j-2] : 0;
            DP[i][j] = max({DP[i-1][j], DP[i-1][j-1] + A[i], base + A[i] + A[i-1] + B[i-1]});
        }
    }

    for (int i=0; i<N; i++)
        cout << DP[N-1][i] << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<ll> A(N, 0);
    vector<ll> B(N-1, 0);

    for (int i=0; i<N; i++)
        cin >> A[i];
    
    for (int i=0; i<N-1; i++)
        cin >> B[i];
    
    solve(N, A, B);
}