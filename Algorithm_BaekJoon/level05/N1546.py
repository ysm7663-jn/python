import sys

N = int(input())

arr = list(map(int, sys.stdin.readline().split()))

max_score = max(arr)

newScore = []
for score in arr :
    newScore.append(score / max_score * 100)
avg = sum(newScore) / N
print(avg)

     

