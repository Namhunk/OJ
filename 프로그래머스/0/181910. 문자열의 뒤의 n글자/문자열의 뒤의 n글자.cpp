#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int n) {
    string answer = "";
    int d = my_string.size();
    for (int i=d-n; i<d; i++)
        answer += my_string[i];
    return answer;
}