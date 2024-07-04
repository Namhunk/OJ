#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, vector<vector<int>> queries) {
    vector<int> answer;
    int min;
    for (auto q : queries){
        min = 1e6+1;
        for (int i=q[0]; i<=q[1]; i++)
            if (arr[i] > q[2] && arr[i] < min)
                min = arr[i];
        
        if (min == 1e6+1) answer.push_back(-1);
        else answer.push_back(min);
    }
    return answer;
}