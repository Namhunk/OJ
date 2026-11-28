# include <iostream>
# include <vector>
# include <algorithm>

using namespace std;
using ll = long long;

void solve(int N, vector<ll>& A, vector<ll>& B){
    const ll neg = -1e18;
    vector<vector<vector<ll>>> DP(N, vector<vector<ll>>(N+1, vector<ll>(3, neg)));
    DP[0][0][0] = 0;
    DP[0][1][1] = A[0];

    for (int i=1; i<N; i++){
        for (int j=0; j<N+1; j++){
            DP[i][j][0] = max({DP[i-1][j][0], DP[i-1][j][1], DP[i-1][j][2]});

            if (j >= 1){
                DP[i][j][1] = max({DP[i-1][j-1][0], DP[i-1][j-1][1], DP[i-1][j-1][2]}) + A[i];
                DP[i][j][2] = DP[i-1][j-1][1] + A[i] + B[i-1];
            }
        }
    }

    for (int j=1; j<N+1; j++)
        cout << max({DP[N-1][j][0], DP[N-1][j][1], DP[N-1][j][2]}) << '\n';

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