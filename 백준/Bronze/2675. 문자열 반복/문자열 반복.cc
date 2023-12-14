#include <iostream>
#include <string>
using namespace std;

int main() {
	int n, a;
	string b, s;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		for (int j = 0; j < b.length(); j++) {
			for (int k = 0; k < a; k++)
				s += b[j];
		}
		cout << s;
		s = "";
		cout << endl;
	}

}