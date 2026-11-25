# include <iostream>
# include <vector>
# include <utility>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, K;
    cin >> N >> K;
    
    long long p=10, r=0;

    for (long long i=1; i<=N; i++){
        if (i == p)
            p *= 10;
        
        r = (r * p + i) % K;
    }

    cout << r;
}