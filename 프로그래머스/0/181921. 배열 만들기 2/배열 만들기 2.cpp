#include <string>
#include <vector>
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

vector<int> solution(int l, int r) {
    // 1 <= l <= r <= 1e6
    vector<int> answer;
    deque<int> que = {5};
    int num = 0;
    while (num <= r){
        num = que[0];
        que.pop_front();
        if (l <= num && num <= r) answer.push_back(num);
        que.push_back(num*10);
        que.push_back(num*10+5);
    }
    if (answer.size() == 0) answer.push_back(-1);
    
    return answer;
}