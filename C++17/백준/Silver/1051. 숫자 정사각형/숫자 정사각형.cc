# include <iostream>
# include <algorithm>
using namespace std;

bool check(int x, int y, int k, char arr[][51]) {
    if (arr[x][y] == arr[x][y + k] &&
        arr[x][y] == arr[x + k][y] &&
        arr[x][y] == arr[x + k][y + k]) {
        return true;
    }
    return false;
}

int main() {
    int N, M;
    scanf("%d %d", &N, &M);

    int ans = 1;
    char arr[50][51];

    int K = min(N, M);

    for (int i = 0; i < N; i++) {
        scanf("%s", arr[i]);
    }

    for (int k = K - 1; k > 0; k--) {
        for (int i = 0; i < N - k; i++) {
            for (int j = 0; j < M - k; j++) {
                if (check(i, j, k, arr)) {
                    ans = max(ans, (k + 1) * (k + 1));
                }
            }
        }
    }

    printf("%d\n", ans);
}
