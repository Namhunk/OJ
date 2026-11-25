# include <iostream>
# include <vector>
# include <utility>

using namespace std;

const int N = 9;

int getUsed(int i, int j, vector<vector<int>>& rows, vector<vector<int>>& cols, bool used[10]) {
    for (int n = 0; n <= 9; n++) used[n] = false;

    for (int k = 0; k < N; k++) {
        used[rows[i][k]] = true; // 같은 행
        used[cols[j][k]] = true; // 같은 열
    }

    int si = 3 * (i / 3);
    int sj = 3 * (j / 3);
    for (int a = si; a < si + 3; a++)
        for (int b = sj; b < sj + 3; b++)
            used[rows[a][b]] = true; // 같은 3x3 칸

    int cnt = 0;
    for (int n = 1; n <= 9; n++)
        if (!used[n]) cnt++;
    return cnt;
}

bool solve(int x, vector<vector<int>>& rows, vector<vector<int>>& cols,
           vector<pair<int,int>>& cand) {
    if (x >= (int)cand.size()) {
        for (auto& r : rows) {
            for (int j = 0; j < N; j++) {
                cout << r[j] << (j < N - 1 ? ' ' : '\n');
            }
        }
        return true;
    }

    bool used[10];
    int best = x, bestCnt = 10;
    for (int k = x; k < (int)cand.size(); k++) {
        int cnt = getUsed(cand[k].first, cand[k].second, rows, cols, used);
        if (cnt < bestCnt) { bestCnt = cnt; best = k; }
        if (cnt <= 1) break;
    }
    if (bestCnt == 0) return false;
    swap(cand[x], cand[best]);

    int i = cand[x].first, j = cand[x].second;
    getUsed(i, j, rows, cols, used);

    for (int n = 1; n <= 9; n++) {
        if (used[n]) continue;

        rows[i][j] = n;
        cols[j][i] = n;

        if (solve(x + 1, rows, cols, cand)) return true;

        rows[i][j] = 0;
        cols[j][i] = 0;
    }
    swap(cand[x], cand[best]);
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<vector<int>> rows(N, vector<int>(N));
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> rows[i][j];

    vector<pair<int,int>> cand;
    vector<vector<int>> cols(N, vector<int>(N, 0));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cols[i][j] = rows[j][i];

            if (rows[i][j] == 0)
                cand.push_back({i, j});
        }
    }

    solve(0, rows, cols, cand);
    return 0;
}