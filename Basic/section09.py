# Section09
# 파일 읽기, 쓰기

# 읽기 모드 r, 쓰기 모드(기존 파일 삭제) w, 추가 모드(파일 생성 또는 추가) a (append)
# 기타 : https://docs.python.org/3.7/library/functions.html#open
# 상대 경로('../', './'), 절대 경로 확인('C:\...')

# 파일 읽기
# 예제1
f = open('./resource/review.txt', 'r')
contents = f.read()
print(contents)
"""
The film, projected in the form of animation,
imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,      
which eventually paves the path for gaining a fresh perspective on an age-old problem.      
The story also happens to centre around two parallel characters, Shundi King and Hundi King,
who are twins, but they constantly fight over unresolved issues planted in their minds      
by external forces from within their very own units.
"""
# print(dir(f))
# 반드시 close 리소스 반환
f.close()

print()

print("----------------------")

# 예제2
# with : 자동으로 close를 반환해준다
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(iter(c))
    # <str_iterator object at 0x000002138A3F7970>
    print(list(c))
    """
    ['T', 'h', 'e', ' ', 'f', 'i', 'l', 'm', ',', ' ', 'p', 'r', 'o', 'j', 'e', 'c', 't', 'e', 'd', ' ', 'i', 'n', ' ', 't', 'h', 'e', ' ', 'f', 'o', 'r', 'm', ' ', 'o', 'f', ' ', 'a', 'n', 'i', 'm', 'a', 't', 'i', 'o', 'n', ',', '\n', 'i', 'm', 'p', 'a', 'r', 't', 's', ' ', 't', 'h', 'e', ' ', 'l', 'e', 's', 's', 'o', 'n', ' ', 'o', 'f', ' ', 'h', 'o', 'w', ' ', 'w', 'a', 'r', 's', ' ', 'c', 'a', 'n', ' ', 'b', 'e', ' ', 'e', 'l', 'u', 'd', 'e', 'd', ' ', 't', 'h', 'r', 'o', 'u', 'g', 'h', ' ', 'r', 'e', 'a', 's', 'o', 
    'n', 'i', 'n', 'g', ' ', 'a', 'n', 'd', ' ', 'p', 'e', 'a', 'c', 'e', 'f', 'u', 'l', ' ', 'd', 'i', 'a', 'l', 'o', 'g', 'u', 'e', 's', ',', '\n', 'w', 'h', 'i', 'c', 'h', ' ', 'e', 'v', 'e', 'n', 't', 'u', 'a', 'l', 'l', 'y', ' ', 'p', 'a', 'v', 'e', 's', ' ', 
    't', 'h', 'e', ' ', 'p', 'a', 't', 'h', ' ', 'f', 'o', 'r', ' ', 'g', 'a', 'i', 'n', 'i', 'n', 'g', ' ', 'a', ' ', 'f', 'r', 'e', 's', 'h', ' ', 'p', 'e', 'r', 's', 'p', 'e', 'c', 't', 'i', 'v', 'e', ' ', 'o', 'n', ' ', 'a', 'n', ' ', 'a', 'g', 'e', '-', 'o', 'l', 'd', ' ', 'p', 'r', 'o', 'b', 'l', 'e', 'm', '.', '\n', 'T', 'h', 'e', ' ', 's', 't', 'o', 'r', 'y', ' ', 'a', 'l', 's', 'o', ' ', 'h', 'a', 'p', 'p', 'e', 'n', 's', ' ', 't', 'o', ' ', 'c', 'e', 'n', 't', 'r', 'e', ' ', 'a', 'r', 'o', 'u', 'n', 'd', ' ', 't', 'w', 'o', ' ', 'p', 'a', 'r', 'a', 'l', 'l', 'e', 'l', ' ', 'c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r', 's', ',', ' ', 'S', 'h', 'u', 'n', 'd', 'i', ' ', 'K', 'i', 'n', 'g', ' ', 'a', 'n', 'd', ' ', 'H', 'u', 'n', 'd', 'i', ' ', 'K', 'i', 'n', 'g', ',', '\n', 'w', 'h', 'o', ' ', 'a', 'r', 'e', ' ', 't', 'w', 'i', 'n', 's', ',', ' ', 'b', 'u', 't', ' ', 't', 'h', 'e', 'y', ' ', 'c', 'o', 'n', 's', 't', 'a', 'n', 't', 'l', 'y', ' ', 'f', 'i', 'g', 'h', 't', ' ', 'o', 'v', 'e', 'r', ' ', 'u', 'n', 'r', 'e', 's', 'o', 'l', 'v', 'e', 'd', ' ', 'i', 's', 's', 'u', 'e', 's', ' ', 'p', 'l', 'a', 'n', 't', 'e', 'd', ' ', 'i', 'n', ' ', 't', 'h', 'e', 'i', 'r', ' ', 'm', 'i', 'n', 'd', 's', '\n', 'b', 'y', ' ', 'e', 'x', 't', 'e', 'r', 'n', 'a', 'l', ' ', 'f', 'o', 'r', 'c', 'e', 's', ' ', 'f', 'r', 'o', 'm', ' ', 'w', 'i', 't', 'h', 'i', 'n', ' ', 't', 'h', 'e', 'i', 'r', ' ', 'v', 'e', 'r', 'y', ' ', 'o', 'w', 'n', ' ', 'u', 'n', 'i', 't', 's', '.']
    """
    print(c)
    """
    The film, projected in the form of animation,
    imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
    which eventually paves the path for gaining a fresh perspective on an age-old problem.
    The story also happens to centre around two parallel characters, Shundi King and Hundi King,
    who are twins, but they constantly fight over unresolved issues planted in their minds
    by external forces from within their very own units.
    """

print()

print("----------------------")

# read : 전체 내용 읽기, read(10) : 10글자 읽기

# 예제3

with open('./resource/review.txt', 'r') as f:
    for c in f:
        # print(c)
        # strip() : 양쪽 공백을 제거해줌, 줄바꿈도 제거
        print(c.strip())
        

print()

print("----------------------")

# 예제4
with open('./resource/review.txt', 'r') as f:
    contents = f.read()
    print('>', contents)
    contents = f.read()  # 내용 없음
    print('>', contents)  # 내용 없음
    f.seek(0, 0)
    contents = f.read()
    print('>', contents)

# readline : 한 줄씩 읽기, readline(문자수) : 문자수 읽기

print()

print("----------------------")
print("----------------------")

# 예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end='###')
        """
        The film, projected in the form of animation,
        ###imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
        ###which eventually paves the path for gaining a fresh perspective on an age-old problem.
        ###The story also happens to centre around two parallel characters, Shundi King and Hundi King,
        ###who are twins, but they constantly fight over unresolved issues planted in their minds
        ###by external forces from within their very own units.###
        """
        line = f.readline()

# readlines : 전체 읽은 후 라인 단위 리스트 저장

print()
print()

print("----------------------")
print("----------------------")

# 예제6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    """
    리스트 형태로 출력
    ['The film, projected in the form of animation,\n', 'imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,\n', 'which eventually paves the path for gaining a fresh perspective on an age-old problem.\n', 'The story also happens to centre around two parallel characters, Shundi King and Hundi King,\n', 'who are twins, but they constantly fight over unresolved issues planted in their minds\n', 'by external forces from within their very own units.']
    """
    print()
    for c in contents:
        print(c, end='*****')
    
    """
    The film, projected in the form of animation,
    *****imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
    *****which eventually paves the path for gaining a fresh perspective on an age-old problem.
    *****The story also happens to centre around two parallel characters, Shundi King and Hundi King,
    *****who are twins, but they constantly fight over unresolved issues planted in their minds
    *****by external forces from within their very own units.*****
    """


print()
print()

# 예제7
with open('./resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line))
        # txt에 저장돼있는건 무조건 문자로 저장돼있기 때문에 int로 형변환
    print(score)
    # [95, 78, 92, 89, 100, 66]
    print('Average : {:6.3f}'.format(sum(score) / len(score)))
    # Average : 86.667

# 파일 쓰기

# 예제1
with open('./resource/test.txt', 'w') as f:
    f.write('niceman!')

# 예제2
with open('./resource/test.txt', 'a') as f:
    f.write('niceman!!')

# 예제3
from random import randint

with open('./resource/score2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(50, 100)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/test2.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Lee\n']
    f.writelines(list)

# 예제5
with open('./resource/test3.txt', 'w') as f:
    print('Test Contents!', file=f)
    print('Test Contents!!', file=f)
