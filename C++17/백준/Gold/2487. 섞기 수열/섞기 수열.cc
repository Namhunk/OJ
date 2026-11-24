# include <iostream>
# include <vector>
# include <numeric>

using namespace std;

long long gcd(long long a, long long b){
    while (b != 0){
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

long long lcm(long long a, long long b){
    if (a == 0 || b == 0) return 0;
    return (a / gcd(a, b)) * b;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    
    vector<int> arr;
    arr.push_back(0);

    vector<int> A = {0};
    for (int i=1; i<N+1; i++){
        int k;
        cin >> k;
        arr.push_back(k);
        A.push_back(i);
    }
    
    vector<bool> visit(N+1, false);
    long long answer = 1;

    for (int i=1; i<N+1; i++){
        if (visit[i]) continue;

        int j, L = 0;
        j = i;

        while (!visit[j]){
            visit[j] = true;
            j = arr[j];
            L++;
        }

        answer = lcm(answer, L);
    }   

    cout << answer;
}   
