# 1 <= n <= 20
import re
def solution(word, pages):
    answer = 0
    n = len(pages)
    
    scores = {}
    for i in range(n):
        # 현재 페이지 이름
        url = re.search(r'<meta[^>]*og:url[^>]*content="(.*?)"', pages[i]).group(1)
        
        # 외부 페이지 목록
        links = re.findall(r'<a\s+href="(https://[^"]*)"', pages[i])
        
        # 검색어 등장 횟수(기본점수)
        count = len(re.findall(rf'(?<![a-zA-Z]){word}(?![a-zA-Z])', pages[i], re.I))
        
        scores[url] = {
            'base':         count,       # 기본점수
            'links':        links,       # 링크 목록
            'links_cnt':    len(links),  # 외부 링크 수
            'index':        i,           # 인덱스 번호
            'matching':     count        # 매칭점수
        }
    for k in scores.keys(): # 모든 key값 사용
        for ln in scores[k]['links']:
            if ln in scores.keys():
                scores[ln]['matching'] += (scores[k]['base'] / scores[k]['links_cnt'])
    
    
    max_score = 0
    for k in scores.keys():
        k_score = scores[k]['matching']
        k_idx = scores[k]['index']
        if k_score > max_score:
            max_score = k_score
            answer = k_idx
        
        print(k, k_idx, k_score, scores[k]['base'])
            
    return answer

'''
기본점수: 검색어 등장 횟수(대소문자 무시)
외부 링크 수: 다른 외부 페이지로 연결된 링크 수
링크점수: 다른 웹페이지 기본점수 / 외부 링크 수
매칭점수: 기본점수 + 링크점수

------------------------------------------------
1. 기본 점수는 괄호 밖 문자 중 word와 일치하는 부분의 개수
2. 현재 웹페이지 정보는 <meta> 태그 내부에 존재
3. 현재 페이지에서 외부 링크는 <a> 태그 내부에 존재
4. 검색어는 대소문자 구분을 무시, 검색어는 알파벳으로만 구성됨
----------------------------------------------
'''