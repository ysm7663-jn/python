"""
3. 삽입 정렬
    1) 삽입 정렬은 두번째 인덱스부터 시작
    2) 해당 인덱스(key 값) 앞에 있는 데이터(B)부터 비교해서 Key 값이 더 작으면, B 값을 뒤 인덱스로 복사
    3) 이를 Key 값이 더 큰 데이터를 만날때까지 반복, 그리고 큰 데이터를 만난 위치 바로 뒤에 key 값을 이동
"""
import random
def insertion_sort(data) :
    for i in range(len(data) - 1) :
        for j in range(i + 1, 0, -1) :
            if data[j] < data[j-1] :
                data[j], data[j-1] = data[j-1], data[j] 
            else :
                break
    return data

data_list = random.sample(range(100), 10)

print(insertion_sort(data_list))
""" 
시간 복잡도 : O(n^2)
    n * (n - 1) / 2
"""