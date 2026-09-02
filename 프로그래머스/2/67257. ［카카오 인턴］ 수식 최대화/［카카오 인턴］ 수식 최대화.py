# 3 <= n <= 100
import re
from itertools import permutations
def solution(expression):
    answer = 0
    
    # re를 사용해 숫자, 연산자 구분
    arr   = re.findall(r'\d+|[+*-]', expression)
    ops =  ['+', '-', '*']
    
    for order in permutations(ops): # 연산자 3개의 모든 순서 = 3! 개
        nums = arr[:]
        for op in order: # 우선순위에 따른 처리 순서
            new_nums = [nums[0]]
            i = 1
            
            while i < len(nums):
                if nums[i] == op: # 해당 순서의 연산자인 경우
                    l = int(new_nums.pop())
                    r = int(nums[i+1])
                    
                    if op == '*':
                        new_nums.append(l * r)
                    elif op == '+':
                        new_nums.append(l + r)
                    else:
                        new_nums.append(l - r)
                    
                else:
                    new_nums.append(nums[i])
                    new_nums.append(nums[i+1])
                    
                i += 2
            
            nums = new_nums # 다음 연산자 처리를 위한 갱신
        
        answer = max(answer, abs((nums[0])))
    return answer
    
'''
3가지의 연산문자 만으로 이루어진 연산 수식이 전달됨 (+, -, *)
수식에 포함된 연산자의 우선순위를 자유롭게 재정의하여 가장 큰 숫자를 제출
연산자는 동일한 순위를 가질 수 없음

계산된 결과가 음수라면 절댓값으로 변환해 제출

---------------------------------------------------------------
연산자의 우선순위만을 바꿔서 답을 구해야함
숫자, 연산자는 위치가 고정됨

'''