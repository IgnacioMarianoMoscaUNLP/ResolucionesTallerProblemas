import sys


def longest_increasing_subsequence_length(nums):
    n = len(nums)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)
N=0
while N<1 or N>10:
    N=int(sys.stdin.readline())

A = []
while len(A)<N or len(A)>N:
    A = list(map(int,sys.stdin.readline().strip().split()))
    print(A)
    
result = longest_increasing_subsequence_length(A)
sys.stdout.write(str(result))