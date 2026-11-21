# include <iostream>
# include <algorithm>
# include <vector>
using namespace std;

bool solve(int N, int K, int T, vector<long long>& A){
	sort(A.begin(), A.end());
	
	long long total = 0;
	vector<long long> arr(N+1, 0);
	
	for (int i=0; i < N; i++){
		total += A[i];
		arr[i+1] = arr[i] + A[i];
	}
	
	if (total == 0) return true;
	if (total < K || total % K != 0) return false;
	
	int p;
	p = total / K;

	if (arr[N-p] > T) return false;
	else return true;

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, K, T;
	cin >> N >> K >> T;

	vector<long long> A(N, 0);
	
	for (int i=0; i < N; i++)
		cin >> A[i];
	
	if (solve(N, K, T, A))
		cout << "YES";
	else
		cout << "NO";
	
}