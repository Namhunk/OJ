#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<string> intStrs, int k, int s, int l) {
    vector<int> answer;
    string temp;
    for (auto strs : intStrs){
        temp = "";
        for (int i=s;i<s+l;i++)
            temp += strs[i];
        
        if (stoi(temp) > k)
            answer.push_back(stoi(temp));
    }
    
    return answer;
}