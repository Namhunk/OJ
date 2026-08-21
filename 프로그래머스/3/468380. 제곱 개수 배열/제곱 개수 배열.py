from bisect import bisect_left

def solution(arr, l, r):
    N = len(arr)
    brr_idx = [0]*N
    brr_num = [0]*N
    brr_idx[0] = arr[0]
    brr_num[0] = arr[0]**2
    for i in range(1, N):
        brr_idx[i] = brr_idx[i-1] + arr[i]
        brr_num[i] = brr_num[i-1] + arr[i]**2

    def block_of(pos):
        return bisect_left(brr_idx, pos)

    def range_sum(left, right, s, e):
        return (brr_num[e] - (brr_idx[e]-right)*arr[e]) - (brr_num[s] - (brr_idx[s]-left+1)*arr[s])

    # K 계산
    s = block_of(l)
    e = block_of(r)
    K = range_sum(l, r, s, e)

    # C 계산 (세그먼트 단위로 O(N))
    size = r - l + 1
    T = brr_idx[-1]
    maxLeft = T - size + 1

    C = 0
    left, right = 1, size
    s = block_of(left)
    e = block_of(right)

    while left <= maxLeft:
        seg_end = min(brr_idx[s], brr_idx[e] - size + 1, maxLeft)
        seg_len = seg_end - left + 1

        cur = range_sum(left, left+size-1, s, e)
        slope = arr[e] - arr[s]

        if slope == 0:
            if cur == K:
                C += seg_len
        else:
            diff = K - cur
            if diff % slope == 0:
                t = diff // slope
                if 0 <= t <= seg_len - 1:
                    C += 1

        left = seg_end + 1
        if left > maxLeft:
            break
        right = left + size - 1
        while s < N-1 and left > brr_idx[s]:
            s += 1
        while e < N-1 and right > brr_idx[e]:
            e += 1

    return [K, C]