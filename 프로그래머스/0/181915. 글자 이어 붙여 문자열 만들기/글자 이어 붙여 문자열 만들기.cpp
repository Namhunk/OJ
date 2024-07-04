#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(string my_string, vector<int> index_list) {
    string answer = "";
    for (int idx : index_list)
        answer += my_string[idx];
    return answer;
}