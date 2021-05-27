N = int(input())

length = list(map(int,input().split()))
cost = list(map(int,input().split()))

total_cost = 0
min_cost = cost[0]

for i in range(len(cost)-1):
    if min_cost > cost[i]:
        min_cost = cost[i]
    total_cost += min_cost * length[i]

print(total_cost)