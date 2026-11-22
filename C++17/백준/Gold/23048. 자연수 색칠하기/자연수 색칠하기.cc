# include <iostream>
# include <vector>
# include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, cnt=1;
    cin >> N;

    vector<int> colors(N+1, 0);
    colors[1] = cnt;

    for (int i=2; i < N+1; i++){
        if (colors[i] == 0){
            cnt++;
            for (int j=i; j < N+1; j+=i){
                if (colors[j] == 0)
                    colors[j] = cnt;
            }
        }
    }

    cout << cnt << '\n';
    for (int i=1; i < N+1; i++)
        cout << colors[i] << (i == N ? '\n' : ' ');


}