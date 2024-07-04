#include <string>
#include <vector>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

// bandage = [시전 시간, 초당 회복량, 추가 회복량]
// health = 최대 체력
// attacks = [공격 시간, 피해량]
// 연속으로 시전시간 만큼 회복하면 추가 회복
int solution(vector<int> bandage, int health, vector<vector<int>> attacks) {
    int answer = 0;
    int before = 0;
    int heal = 0;
    int time = 0;
    int hp = health;
    for (int i=0; i<attacks.size(); i++){
        if(hp < health){
            time = attacks[i][0] - before -1;
            heal = (time * bandage[1]) + (time/bandage[0]*bandage[2]);
            hp = min(hp+heal, health);
        }
        
        hp -= attacks[i][1];
        before = attacks[i][0];
        if (hp <= 0) break;
    }
    
    answer = (hp <= 0 ? -1 : hp);
    return answer;
}