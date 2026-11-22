import sys
input = sys.stdin.readline

def solution():
    # 2 <= N <= 100
    N = int(input().strip())
    arr = []
    for i in range(2*N):
        row = ' '*(2*N-i-1) + '*' + ' '*(i+1)
        arr.append(row)
    
    idx = 0
    for i in range(1, N+1):
        row = ' '*(N-i) + '*' + ' '*(i-1)
        row2 = row + ' ' + row[::-1]

        arr[idx] += row2
        idx += 1
    
    for i in range(N, 0, -1):
        row = ' '*(N-i) + '*' + ' '*(i-1)
        row2 = row + ' ' + row[::-1]

        arr[idx] += row2
        idx+=1

    for i in arr:
        print(i)

if __name__ == '__main__':
    solution()

"""

2N행
4N + 2열 크기의 BOJ 로고를 출력

한 행에서 점의 개수 3개

   *  * * 
  *  *   *
 *   *   *
*     * * 

         *     * *    
        *     *   *   
       *     *     *  
      *     *       * 
     *     *         *
    *      *         *
   *        *       * 
  *          *     *  
 *            *   *   
*              * *  


  *
 *
 *
  *
"""