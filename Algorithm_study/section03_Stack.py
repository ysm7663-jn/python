""" 
3. 스택 (Stack)
    데이터를 제한적으로 접근할 수 있는 구조
        > 한쪽 끝에서만 자료를 넣거나 뺄 수 있는 구조
    가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조

1) 스택 구조
    LIFO(Last-In, Fisrt-Out) : 마지막에 넣은 데이터를 가장 먼저 추출하는 데이터 관리 정책
    FILO(First-In, Last-Out) : 처음에 넣은 데이터를 가장 마지막에 추출하는 데이터 관리 정책

    대표적인 스택의 활용 : 컴퓨터 내부의 프로세스 구조의 함수 동작 방식

    주요 기능
     - push() : 데이터를 스택에 넣기
     - pop()  : 데이터를 스택에서 꺼내기
"""
# 재귀 함수
def recursive(data) :
    if data < 0:
        print('ended')
    else :
        print(data)
        recursive(data - 1)
        print("returned", data)
recursive(4)
"""
4
3
2
1
0
ended     
returned 0
returned 1
returned 2
returned 3
returned 4
"""

""" 
3) 자료 구조 스택의 장점
    장점
        구조가 단순해서, 구현이 쉽다
        데이터 저장/읽기 속도가 빠르다
    단점
        데이터 최대 갯수를 미리 정해야 한다.
            > 파이썬의 경우 재귀 함수는 1000번까지만 호출이 가능
        저장 공간의 낭비가 발생할 수 있음
            > 미리 최대 갯수만큼 저장 공간을 확보해야 함
""" 

# 연습 문제 1
data_stack = list()
# data_stack.append() : 데이터 삽입
data_stack.append(1)
data_stack.append(2)

print(data_stack) # [1, 2]
# data_stack.pop() : 가장 나중에 들어간 데이터를 출력 후 삭제
print(data_stack.pop()) # 2

# 연습 문제 2 
# 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기

stack_list = list()

def push(data) :
    stack_list.append(data)

def pop():
    data = stack_list[-1] # 가장 위에 있는 데이터 저장
    del stack_list[-1] # 삭제
    return data # 뽑아 놓은 데이터 저장
for index in range(10) :
    push(index)
print(pop()) # 9