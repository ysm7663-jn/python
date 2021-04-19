N = int(input())

length = list(map(int,input().split()))
cost = list(map(int,input().split()))

total_length = sum(length)
sum = 0

min_cost = 0

for i in range(N-1) :

    for j in range(len(cost)-1) :
        if cost[j] < cost[j+1] :
            min_cost = cost[j]

    print('min_cost', min_cost)

    if cost[i] == min_cost :
        sum += total_length * cost[i]
        print('if',sum)
        break
    else :
        sum += cost[i] * length[i]
        total_length -= length[i]
        print('sum',sum)
        print('total',total_length)
print(sum)

