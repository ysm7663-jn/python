# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import datetime
import sqlite3

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now', now) # now 2021-03-26 15:32:56.658740 / 년 월 일 시 분 초 나노초

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime', nowDatetime) # nowDatetime 2021-03-26 15:32:56

# sqlite3 버전
print('sqlite3.version : ', sqlite3.version) # sqlite3.version :  2.6.0
print('sqlite3.sqlite_version', sqlite3.sqlite_version) # sqlite3.sqlite_version 3.34.0

# DB생성 & Autocommit (Rollback)
# 본인 DB 파일 경로
# isolation_level=None
conn = sqlite3.connect('C:/python_basic/resource/database.db', isolation_level=None)

# DB생성(메모리)
# conn = sqlite3.connect(":memory:")

# Cursor연결
c = conn.cursor()
print('Cursor Type : ', type(c)) # Cursor Type :  <class 'sqlite3.Cursor'>

# 테이블 생성(Datatype : TEXT : 문자열 NUMERIC : 소수 INTEGER : 정수 REAL : realData BLOB : 파일 저장)
c.execute(
    "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")  # AUTOINCREMENT

# 데이터 삽입
# primary key 때문에 중복 생산에 오류가 발생하기 때문에 주석 처리
c.execute("INSERT INTO users VALUES (1 ,'Kim','Kim@naver.com', '010-0000-0000', 'Kim.com', ?)", (nowDatetime,))

c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)",
        (2, 'Park', 'Park@naver.com', '010-1111-1111', 'Park.com', nowDatetime))


# Many 삽입(튜플, 리스트)

userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', nowDatetime)
)
c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)


# 테이블 데이터 삭제
# print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")

# 커밋 : isolation_level=None 일 경우 자동 반영(Auto Commit)
conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
conn.close()