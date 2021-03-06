def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p    
    return participant.pop()

"""
zip(a, b)

numbers = [1, 2, 3]
letters = ["a", "b", "c"]

for pair in zip(numbers, letters):
    print(pair)

(1, "a")
(2, "b")
(3, "c")
"""

"""
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
"""

participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']
print(solution(participant, completion))
print('---')
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))
print('---')
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))