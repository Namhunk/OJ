# include <iostream>
# include <vector>
# include <map>
# include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double tot = 0, ans = 0;
    map<string, double> grade = {
        {"A+", 4.5},
        {"A0", 4.0},
        {"B+", 3.5},
        {"B0", 3.0},
        {"C+", 2.5},
        {"C0", 2.0},
        {"D+", 1.5},
        {"D0", 1.0},
        {"F", 0.0}
    };

    for (int i=0; i<20; i++){
        string a, c;
        double b;
        
        cin >> a >> b >> c;

        if (c == "P") continue;

        ans += (b * grade[c]);
        tot += b;
    }

    cout << fixed;
    cout.precision(6);
    cout << ans / tot;

}