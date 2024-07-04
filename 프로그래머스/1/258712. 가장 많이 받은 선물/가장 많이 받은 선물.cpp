#include <string>
#include <vector>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int solution(vector<string> friends, vector<string> gifts) {
    int answer = 0;
    int MAX = friends.size();
    map<string, int> m;
    int arr[MAX][MAX];
    memset(arr, 0, sizeof(arr));
    for (int i=0; i<MAX; i++)
        m[friends[i]] = i;
    
    int cnt[MAX];
    memset(cnt, 0, sizeof(cnt));
    string x, y;
    for (auto q : gifts){
        stringstream ss(q);
        ss >> x >> y;
        arr[m[x]][m[y]]++;
        cnt[m[x]]++;
        cnt[m[y]]--;
    }
    
    int result[MAX];
    memset(result, 0, sizeof(result));
    
    for (int i=0; i<MAX; i++){
        for (int j=0; j<MAX; j++){
            if (arr[i][j] > arr[j][i]) result[i]++;
            else if (arr[i][j] == arr[j][i] && cnt[i] > cnt[j]) result[i]++;
        }
    }
    
    for (auto r : result)
        answer = max(answer, r);
    return answer;
}