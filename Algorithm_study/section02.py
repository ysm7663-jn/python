"""
2. 큐 (Queue)

1) 큐 구조 
    가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조 (줄을 서는 행위와 유사)
    FIFO, (First-In, First-Out)
    LILO, (Last-In, Last-Out)
    
2) 알아둘 용어
    Enqueue : 큐에 데이터를 넣는 기능
    Dequeue : 큐에서 데이터를 꺼내는 기능
    https://visualgo.net : 기본적인 자료구조를 연습할 수 있음

3) 파이썬 queue 라이브러리 활용해서 큐 자료 구조 사용하기
Queue() : 가장 일반적인 큐 자료 구조
LifoQueue() : 나중에 입력된 데이터가 먼저 출력되는 구조(스택 구조와 유사)
PriorityQueue() : 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력

3-1) Queue()로 큐 만들기
"""
import queue
data_queue = queue.Queue()
# data_queue.put() : queue에 원소 삽입
data_queue.put("funcoding")
data_queue.put(1)
# data_queue.qsize() : queue의 사이즈를 출력
print(data_queue.qsize()) # 2
# data_queue.get() : queue에 있는 원소 출력 후 제거
print(data_queue.get()) # funcoding
print(data_queue.qsize()) # 1
print(data_queue.get()) # 1
print(data_queue.qsize()) # 0
"""
3-2) PriorityQueue()로 큐 만들기
"""
import queue
data_pqueue = queue.PriorityQueue()
data_pqueue.put((10,"korea"))
data_pqueue.put((5,1))
data_pqueue.put((15,"china"))
print(data_pqueue.qsize()) # 3
print(data_pqueue.get()) # (5, 1)  >> 우선순위가 가장 높은거 먼저 출력
print(data_pqueue.get()) # (10, 'Korea')  

"""
장단점은 없지만, 큐의 활용 예로 프로세스 스케줄링 방식을 함께 이해해야 함
"""
# 연습 문제 1
# 리스트 변수로 큐를 다루느 enqueue, dequeue 기능 구현

queue_list = list()

def enqueue(data) :
    queue_list.append(data)
def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for i in range(10) :
    enqueue(i)
print(len(queue_list)) # 10
print(queue_list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(dequeue()) # 0
print(dequeue()) # 1
    
