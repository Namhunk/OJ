# include <iostream>
# include <vector>
# include <numeric>

using namespace std;
using ll = long long;

ll get_cnt(ll N, ll L, ll M, ll X, vector<ll>& A){
    ll k = 0, cnt = 0, cur = 0;

    for (int i=0; i<N; i++){
        if (cur == 0){
            k = i;
        }

        if (i - k + 1 > L){
            cnt += 1;
            cur = 0;
            k = i;
        }

        cur += A[i];
        if (cur >= X){
            cnt += (cur / X);
            cur %= X;
            k = i;
        }

        if (cnt > M)
            return cnt;
    }
    
    if (cur)
        cnt += 1;

    return cnt;
}

ll solve(ll N, ll L, ll M, vector<ll>& A){
    ll lo = 1, hi = accumulate(A.begin(), A.end(), 0LL);
    if (get_cnt(N, L, M, hi, A) > M)
        return -1;

    while (lo < hi){
        ll X = (lo + hi) / 2;

        if (get_cnt(N, L, M, X, A) <= M)
            hi = X;
        else
            lo = X + 1;
    }

    return lo;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll N, M, L;
    vector<ll> A;
    cin >> N >> M >> L;

    for (int i=0; i<N; i++){
        ll num;
        cin >> num;
        A.push_back(num);
    }

    cout << solve(N, L, M, A);
    
}