# include <iostream>
# include <algorithm>
# include <vector>
# include <utility>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int V, E;
    cin >> V >> E;

    vector<vector<pair<int, int>>> G(V+1);
    vector<int> deg(V+1, 0);

    for (int i=0; i < E; i++){
        int a, b;
        cin >> a >> b;
        G[a].push_back({b, i});
        G[b].push_back({a, i});
        deg[a]++;
        deg[b]++;

    }

    vector<int> odd;

    for (int i=1; i <= V; i++)
        if (deg[i] % 2 != 0)
            odd.push_back(i);
    
    if (odd.size() != 0 && odd.size() != 2){
        cout << "NO";
        return 0;
    }

    int start = 0;
    if (!odd.empty())
        start = odd[0];
    else{
        for (int i=0; i < V; i++)
            if (deg[i] > 0){
                start = i;
                break;
            }
        }
    
    vector<bool> used(E, false);
    vector<int> stack = {start};
    vector<int> path;

    while (!stack.empty()){
        int u = stack.back();

        while (!G[u].empty() && used[G[u].back().second])
            G[u].pop_back();
        
        if (!G[u].empty()){
            int v = G[u].back().first;
            int idx = G[u].back().second;
            G[u].pop_back();

            used[idx] = true;
            stack.push_back(v);
        }
        else{
            path.push_back(stack.back());
            stack.pop_back();
        }
    }

    if (path.size() == E+1){
        cout << "YES";
    }
    else{
        cout << "NO";
    }

    return 0;
}
