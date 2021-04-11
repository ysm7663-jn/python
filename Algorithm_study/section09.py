"""
1. 버블 정렬
for index in range(데이터 길이 - 1) :
    for index2 in range(데이터 길이 - index - 1):
        if 앞데이터 > 뒤데이터 :
            swap(앞데이터, 뒤데이터)
"""
import random
def bubblesort(data) :
    for i in range(len(data) - 1) :
        swap = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j+1] :
                data[j], data[j+1] = data[j+1], data[j]
                swap = True
        if swap == False :
            break
    return data
data_list = random.sample(range(100),50)
print(bubblesort(data_list))

"""
시간 복잡도 : O(n^2)
    최악의 경우 : n * (n - 1) / 2 
정렬이 돼있는 경우 : O(n)

"""
