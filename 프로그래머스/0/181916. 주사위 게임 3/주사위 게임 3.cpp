#include <string>
#include <vector>
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int solution(int a, int b, int c, int d) {
    int answer = 0;
    vector<int> v(7, 0);
    set<int> s = {a, b, c, d};
    v[a]++;
    v[b]++;
    v[c]++;
    v[d]++;
    
    int MAX = *max_element(v.begin(), v.end());
    
    if (MAX == 4) answer = 1111*a;
    else if (MAX == 3){
        for (int i=1; i<7; i++)
            if (v[i] == 1) answer += i;
            else if (v[i] == 3) answer += (10*i);
        answer = answer*answer;
    }
    else if (MAX == 2 && s.size() == 2){
        int num1 = 0;
        int num2 = 0;
        for (int i=1; i<7; i++)
            if (v[i] == 2){
                if (!num1) num1 = i;
                else num2 = i;
            }
        answer = (num1 + num2) * abs(num1-num2);
    }
    else if (MAX == 2 && s.size() == 3){
        answer = 1;
        for (int i=1; i<7; i++)
            if (v[i] == 1) answer *= i;
    }
    else{
        answer = 7;
        for (int i=1; i<7; i++)
            if (v[i] == 1) answer = min(answer, i);
    }
        
    return answer;
}