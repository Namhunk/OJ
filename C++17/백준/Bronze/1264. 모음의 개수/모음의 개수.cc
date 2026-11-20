# include <iostream>
# include <string>
# include <set>
# include <cctype>

using namespace std;

int main(){
	string S;
	set<char> keys = {'a', 'e', 'i', 'o', 'u'};
	int cnt;
	while (1){
		cnt = 0;
		getline(cin, S);
		if (S.size() == 1 && S[0] == '#') break;
		
		for (auto& x: S) {
			x = tolower(x);
			if (keys.count(x)) {cnt++;}
			
		}
		cout << cnt << '\n';
	}

}