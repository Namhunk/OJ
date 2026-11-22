# include <iostream>
# include <algorithm>
# include <vector>
using namespace std;

void solve(int N, vector<int>& arr){
    if (N < 2){ // 2보다 작은 경우
        cout << 'A';
    }
    else{
        if (count(arr.begin(), arr.end(), arr[0]) == N){ // 모두 같은 숫자인 경우
            cout << arr[0];
        }
        else{
            if (N < 3){
                cout << 'A';
            }
            else{
                if (arr[1]-arr[0] == 0){
                    cout << 'B';
                }
                else{
                    double A, B;
                    A = (double)(arr[2]-arr[1]) / (arr[1]-arr[0]);
                    B = arr[1] - arr[0]*A;

                    int a = A, b = B;
                    if (a != A || b != B){
                        cout << 'B';
                    }
                    else{
                        int flag = 1, cur = 0;
                        cur = arr[0]*a + b;

                        for (int i=1; i < N; i++){
                            if (cur != arr[i]){
                                flag = 0;
                                break;
                            }

                            cur = arr[i]*a + b;
                        }

                        if (!flag)
                            cout << 'B';
                        else
                            cout << arr[N-1]*a+b;
                    }
                }

            }
        }

    }

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    
    vector <int> arr(N, 0);
    for (int& x: arr)
        cin >> x;
    
    solve(N, arr);
}