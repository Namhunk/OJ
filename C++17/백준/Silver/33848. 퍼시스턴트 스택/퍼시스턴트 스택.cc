# include <iostream>
# include <vector>
# include <utility>
# include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int Q;
    cin >> Q;

    vector<pair<int, long long>> history;
    vector<long long> stack;

    for (int i=0; i<Q; i++){
        int a;
        long long b;
        cin >> a;

        switch (a){
            case 1:
                cin >> b;
                stack.push_back(b);
                history.push_back({a, b});
                break;
            case 2:
                b = stack.back();
                stack.pop_back();
                history.push_back({a, b});
                break;
            case 3:
                cin >> b;
                for (int j=0; j<b; j++){
                    auto [x, y] = history.back();
                    history.pop_back();

                    if (x == 1)
                        stack.pop_back();
                    else
                        stack.push_back(y);
                }
                break;
            case 4:
                cout << stack.size() << '\n';
                break;
            case 5:
                cout << (stack.size() != 0 ? stack.back() : -1) << '\n';
                break;
        }
    }
}