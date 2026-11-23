# include <iostream>
# include <algorithm>
# include <vector>
# include <utility>
# include <cmath>
# include <string>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, k=10, r=0;
    cin >> N;

    N--;
    
    while (N >= (k-1)*pow(k, r)*(r+1)){
        N -= (k-1)*pow(k, r)*(r+1);
        r++;
    }

    double div = floor(N/(r+1));
    int mod = N % (r+1);

    long long num = (pow(10, r) + div);
    string S = to_string(num);

    cout << S[mod];
}   
