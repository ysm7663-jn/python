# Section11
# 파이썬 예외처리의 이해
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) Header 스킵 >> 1번 라인(첫 번째줄) 스킵
    # 확인
    print(reader) # <_csv.reader object at 0x0000021D9F806640>
    print(type(reader)) # <class '_csv.reader'>
    print(dir(reader))  # __iter__ 확인 >> 반복문에서 사용할 수 있다
    print()

    for c in reader:
        print(c)
    """
    ['번호', '이름', '가입일시', '나이']
    ['1', '김정수', '2017-01-19 11:30:00', '25']
    ['2', '박민구', '2017-02-07 10:22:00', '35']
    ['3', '정순미', '2017-01-22 09:10:00', '33']
    ['4', '김정현', '2017-02-22 14:09:00', '45']
    ['5', '홍미진', '2017-04-01 18:00:00', '17']
    ['6', '김순철', '2017-05-14 22:33:07', '22']
    ['7', '이동철', '2017-03-01 23:44:45', '27']
    ['8', '박지숙', '2017-01-11 06:04:18', '30']
    ['9', '김은미', '2017-02-08 07:44:33', '51']
    ['10', '장혁철', '2017-12-01 13:01:11', '16']
    """

# 예제2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')  # 구분자 선택
    # next(reader) Header 스킵
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ 확인
    print()

    for c in reader:
        print(c)
    """
    ['번호', '이름', '가입일시', '나이']
    ['1', '김정수', '2017-01-19 11:30:00', '25']
    ['2', '박민구', '2017-02-07 10:22:00', '35']
    ['3', '정순미', '2017-01-22 09:10:00', '33']
    ['4', '김정현', '2017-02-22 14:09:00', '45']
    ['5', '홍미진', '2017-04-01 18:00:00', '17']
    ['6', '김순철', '2017-05-14 22:33:07', '22']
    ['7', '이동철', '2017-03-01 23:44:45', '27']
    ['8', '박지숙', '2017-01-11 06:04:18', '30']
    ['9', '김은미', '2017-02-08 07:44:33', '51']
    ['10', '장혁철', '2017-12-01 13:01:11', '16']
    """

# 예제3 (Dict 변환)
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)
    # 확인
    #print(reader)
    #print(type(reader))
    #print(dir(reader))  # __iter__ 확인
    
    print()

    #for c in reader:
    #   print(c)
    
    """
    {'번호': '1', '이름': '김정수', '가입일시': '2017-01-19 11:30:00', '나이': '25'}
    {'번호': '2', '이름': '박민구', '가입일시': '2017-02-07 10:22:00', '나이': '35'}
    {'번호': '3', '이름': '정순미', '가입일시': '2017-01-22 09:10:00', '나이': '33'}
    """
    
    for c in reader:
        for k, v in c.items():
            print(k, v) 
        print("---------")
    """
    번호 1
    이름 김정수
    가입일시 2017-01-19 11:30:00
    나이 25
    ---------
    번호 2
    이름 박민구
    가입일시 2017-02-07 10:22:00
    나이 35
    ---------
    번호 3
    이름 정순미
    가입일시 2017-01-22 09:10:00
    나이 33
    ---------
    """

# 예제4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

with open('./resource/sample3.csv', 'w') as f:  # newline='' 테스트
    wt = csv.writer(f)
    # dir 확인
    print(dir(wt))
    print(type(wt))
    # 데이터의 검증이 필요한 경우 사용
    for v in w:
        wt.writerow(v)
    """
    newline='' 이 없을 경우
    1,2,3

    4,5,6

    7,8,9

    10,11,12

    13,14,15


    """

# 예제5
with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    # dir 확인
    print(dir(wt)) 
    print(type(wt)) # <class '_csv.writer'>

    # for 필요없이 한번에 작성 / 데이터의 검증이 필요 없는 경우
    wt.writerows(w)

    """
    1,2,3
    4,5,6
    7,8,9
    10,11,12
    13,14,15
    """

# XSL, XLSX : MIME - applications/vnd.excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
# pip install pandas 설치 필요
# pip install xlrd   설치 필요
# pip install openpyxl 설치 필요

# openpyxl, xlsxwriter, xlrd, xlwt, xlutils 등 있으나 pandas를 주로 사용(openpyxl, xlrd) 포함

import pandas as pd

# sheetname = '시트명' 또는 숫자, header=숫자, skiprow=숫자  
xlsx = pd.read_excel('./resource/sample.xlsx') 
# xlsx = pd.read_excel('./resource/sample.xlsx', skiprow=1) 
# 첫 번째 줄 킵

# 상위 데이터 확인
# 상위 5개만 출력
print(xlsx.head())
print()

# 데이터 확인
# 하위 5개만 출력
print(xlsx.tail())
print()

# 데이터 구조
print(xlsx.shape) # 행, 열 / (20, 7)

# 데이터 전체 확인
print(xlsx) 

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)