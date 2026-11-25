# include <iostream>
# include <vector>
# include <utility>
# include <string>
# include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    
    vector<vector<int>> arr(N, vector<int>(N, 0));

    for (int i=0; i<N; i++){
        string S;
        cin >> S;
        for (int j=0; j<N; j++){
            if (S[j] == 'Y')
                arr[i][j] = 1;
        }
    }

    vector<vector<int>> ans(N, vector<int>(N, 0));
    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++)
            if (arr[i][j] ==1 && arr[j][i] == 1)
                ans[i][j] = 1;
    
    for (int k=0; k<N; k++)
        for (int i=0; i<N; i++)
            for (int j=0; j<N; j++){
                if (i == j) continue;
                if (arr[i][k] ==1 && arr[k][i] == 1 && arr[j][k] == 1 && arr[k][j] == 1)
                    ans[i][j] = 1;
            }
    
    int ret = 0;
    for (auto& x: ans){
        int cnt = count(x.begin(), x.end(), 1);
        ret = max(ret, cnt);
    }

    cout << ret;
}