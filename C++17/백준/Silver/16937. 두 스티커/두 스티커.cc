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

    int H, W, N;

    cin >> H >> W;
    cin >> N;

    vector<vector<int>> arr;
    for (int i=0; i < N; i++){
        int R, C;
        cin >> R >> C;

        if (R <= H && C <= W)
            arr.push_back({R, C, R*C, i});
        
        if (C <= H && R <= W)
            arr.push_back({C, R, R*C, i});
    }

    int ans = 0;
    for (int x=0; x < arr.size(); x++){
        int nH, nW;
        nH = H-arr[x][0]; nW = W-arr[x][1];

        for (int y=0; y < arr.size(); y++){
            if (arr[x][3] == arr[y][3]) continue;

            if (arr[y][0] <= nH && arr[y][1] <= W)
                ans = max(ans, arr[x][2]+arr[y][2]);
            
            if (arr[y][0] <= H && arr[y][1] <= nW)
                ans = max(ans, arr[x][2]+arr[y][2]);
        }
    }

    cout << ans;
}   
