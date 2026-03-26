# 가상 환경 생성

# MAC 기준
# python3 -m venv .venv
# source .venv/bin/activate
# pip install --upgrade pip

# Window기준
# python -m venv .venv
# ./venv/Scripts/Activate
# pip install --upgrade pip

# pymysql설치(잠깐 대기!!!)
# pip install pymysql

# Workbench에서 연결 정보 확인
# host: 127.0.0.1             # 워크벤치 홈에서 일치하나 확인
# prot: 3306
# user: root
# database: health_ai

# DB 연결

import pymysql  # my sql(CLI) > python(mysql) 작업

#conn = pymysql.connect(
#    host = 'localhost',
#    user = 'root',
#    password = 'tlswlWkd23',
#    db = 'health_ai',
#    charset = 'utf8mb4',
#    cursorclass=pymysql.cursors.DictCursor
#)

# with - as (안전)
#cursor = conn.cursor()

#with conn.cursor() as cursor:
#    cursor.execute("SHOW TABLES;")
#    print(cursor.fetchall())
#cursor.close()

# cursor.execute("SHOW TABLES;")
# print(cursor.fetchall())
# [{'Tables_in_health_ai': 'diagnosis'}, 
# {'Tables_in_health_ai': 'patients'}, 
# {'Tables_in_health_ai': 'visits'}]
# cursor.close()

# patients 테이블 조회
#with conn.cursor() as cursor: # 파이썬에서는 커서 있어야 데이터베이스 조회 가능
#     cursor.execute("SELECT * FROM patients;")
#     row = cursor.fetchone() # 한 줄만
#     print(row)
#     print("\n")

#     rows = cursor.fetchmany(5) # 5줄 확인
#     print(rows)
#conn.close()
 
# with conn.cursor() as cur:
#    # 1) CREATE TABLE
#    cur.execute("""
#    CREATE TABLE patient_info (
#	id INT AUTO_INCREMENT PRIMARY KEY,
#    name VARCHAR(50) NOT NULL,
#    gender CHAR(1),
#    birth_date DATE,
#    city VARCHAR(50) DEFAULT 'Unknown'
#    );
#    """)
#    conn.commit()

# conn.close()

# 2) INSERT

# 3) UPDATE

# 4) DELETE

# conn.commit()

# 튜플 데이터 타입
data = (1,2,3)
print(data)

# 튜플은 데이터 1개 담을 때 data = (1,) 이런 식으로 , 찍어줘야 함.
