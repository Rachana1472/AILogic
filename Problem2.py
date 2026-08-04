import collections
import sys

def solve(n, arr, k):
    max_dq = collections.deque() 
    min_dq = collections.deque() 

    left = 0
    max_len = 0
    best_start = 1

    for right in range(n):
        val = arr[right]
        while max_dq and arr[max_dq[-1]] <= val:
            max_dq.pop()
        max_dq.append(right)
        while min_dq and arr[min_dq[-1]] >= val:
            min_dq.pop()
        min_dq.append(right)
        while arr[max_dq[0]] - arr[min_dq[0]] > k:
            if max_dq[0] == left:
                max_dq.popleft()
            if min_dq[0] == left:
                min_dq.popleft()
            left += 1

        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            best_start = left + 1 

    return max_len, best_start

def test():
    n, arr, k = 8, [4, 2, 2, 3, 1, 5, 4, 2], 2
    res = solve(n, arr, k)
    print("Sample:", res, "Expected: (4, 1)")
    assert res == (4, 1)
    n, arr, k = 5, [3, 3, 3, 3, 3], 0
    res = solve(n, arr, k)
    print("Identical:", res, "Expected: (5, 1)")
    assert res == (5, 1)
    n, arr, k = 3, [10, 100, 1000], 5
    res = solve(n, arr, k)
    print("No adjacent:", res, "Expected: (1, 1)")
    assert res == (1, 1)
    n, arr, k = 4, [-5, -3, -4, -10], 2
    res = solve(n, arr, k)
    print("Negative:", res, "Expected: (3, 1)")
    assert res == (3, 1)
    n, arr, k = 6, [10, 20, 1, 2, 30, 40], 1
    res = solve(n, arr, k)
    print("Tie breaker:", res, "Expected: (2, 3)")
    assert res == (2, 3)
    print("All unit tests passed!")
if __name__ == "__main__":
    test()

