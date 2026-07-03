# [level 5] 가짜 해밀토니안 - 70132 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/70132) 

### 성능 요약

메모리: 100 MB, 시간: 783.88 ms

### 구분

코딩테스트 연습 > 월간 코드 챌린지 시즌1

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 07월 03일 15:55:35

### 문제 설명

<p>다음 조건을 만족하는 그래프 상의 <a href="https://en.wikipedia.org/wiki/Path_(graph_theory)" target="_blank" rel="noopener">경로(Path)</a>를 <strong>가짜 해밀토니안 경로</strong>라고 정의합니다.</p>

<ul>
<li>경로가 그래프 상의 모든 점을 최소 1번, 최대 2번 방문해야 합니다.</li>
</ul>

<p>그래프의 형태에 따라, 해당 그래프가 가짜 해밀토니안 경로를 가질 수도 있고, 가지지 않을 수도 있습니다. 본 문제에서 주어지는 그래프는 항상 트리 형태이며, 다음은 트리에서 가짜 해밀토니안 경로를 나타내는 예시입니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/e2cd7da9-b86e-4946-b122-9f4672c3c075/expand1.png" title="" alt="expand1.png"></p>

<ul>
<li>이 트리는 가짜 해밀토니안 경로를 가지는 트리입니다. 그림의 경로가 트리 상의 모든 점을 최소 1번, 최대 2번 방문하는 가짜 해밀토니안 경로 중 하나입니다.</li>
</ul>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/91670de9-624c-4e48-a763-da24a7fe0b14/expand2.png" title="" alt="expand2.png"></p>

<ul>
<li>이 트리는 가짜 해밀토니안 경로를 가지지 않는 트리입니다.</li>
</ul>

<p>트리 정보를 담고 있는 2차원 정수 배열 t가 매개변수로 주어집니다. 이 트리의 모든 <a href="https://en.wikipedia.org/wiki/Tree_(data_structure)#Terminology" target="_blank" rel="noopener">부분 트리(Subtree)</a> 중에서, 가짜 해밀토니안 경로를 갖고 있으면서 동시에 점의 개수가 제일 많은 트리의 크기를 찾아 그 트리의 점의 개수를 return 하도록 solution 함수를 완성해주세요.</p>

<p>이때, 점의 개수가 3 이상(제한사항을 참고해주세요)인 임의의 트리는 항상 가짜 해밀토니안 경로를 가지는 부분 트리를 가지므로, 이 문제에서 답은 항상 존재합니다.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>t의 행의 개수는 2 이상 200,000 미만입니다.

<ul>
<li>트리의 점(Vertex)의 개수는 (t의 행의 개수 + 1) 입니다. 즉, 트리의 점의 개수는 3 이상 200,000 이하입니다.</li>
<li>각 행은 [v1, v2] 2개의 정수로 이루어져 있습니다.</li>
<li>이는 v1번 점과 v2번 점이 서로 연결되어 있다는 것을 의미합니다.</li>
<li>v1, v2는 각각 0 이상 (t의 행의 개수) 이하입니다.</li>
<li>v1과 v2는 서로 다른 수입니다.</li>
<li>t는 항상 트리 형태로만 주어집니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>t</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td><code>[[5,1],[2,5],[3,5],[3,6],[2,4],[4,0]]</code></td>
<td>7</td>
</tr>
<tr>
<td><code>[[2,5],[2,0],[3,2],[4,2],[2,1]]</code></td>
<td>4</td>
</tr>
</tbody>
      </table>
<hr>

<p>입출력 예 #1</p>

<ul>
<li>주어진 트리를 그림으로 나타내면 다음과 같습니다.
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/01d3d496-5cdd-4717-9b06-d1c70eb4788a/ex1.png" title="" alt="ex1.png"></li>
<li>이 트리는 그 자체로 가짜 해밀토니안 경로를 가지므로, 트리의 점의 개수인 7을 return 해야 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>주어진 트리에서, 가짜 해밀토니안 경로를 가지면서 점의 개수가 가장 많은 부분 트리 중 하나를 그림으로 나타내면 다음과 같습니다.
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/43eb6221-a5eb-4150-b4f6-1e0f1fb721d3/ex2.png" title="" alt="ex2.png"></li>
<li><code>(0,1,2,3)</code> 외에도 <code>(0,2,4,5)</code>, <code>(1,2,3,4)</code> 등 가짜 해밀토니안 경로를 가지면서 점의 개수가 4개인 다른 부분 트리가 존재하지만, 동일한 조건에서 그보다 더 많은 점의 개수를 가지는 트리는 없습니다.</li>
<li>따라서 4를 return 해야 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges