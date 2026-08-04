def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    intervals = []
    idx = 1
    for _ in range(n):
        start, end = int(data[idx]), int(data[idx+1])
        intervals.append((start, end))
        idx += 2
    intervals.sort(key=lambda x: x[0])
    curr_start, curr_end = intervals[0]
    for start, end in intervals[1:]:
        if start <= curr_end:
            curr_end = max(curr_end, end)
        else:
            print(f"{curr_start} {curr_end}")
            curr_start, curr_end = start, end
    print(f"{curr_start} {curr_end}")
if __name__ == "__main__":
    main()
