def solution(num_list):
    answer = num_list + [num_list[-1] - num_list[-2] if num_list[-1] > num_list[-2] else num_list[-1]*2]
    return answer