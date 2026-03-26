# 가상환경 생성
# python3 -m venv .venv
# source .venv/bin/activate
# pip install --upgrade pip

# pymysql설치
# pip install pymysql

# Workbench에서 연결 정보 확인
# host: 127.0.0.1
# port: 3306
# user: root
# database: health_ai

# DB연결
import pandas as pd
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="test1234",
    db='health_ai',
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

# 1) CSV 파일을 pandas로 읽기
df = pd.read_csv("health_train.csv")
print(df.shape)
print(df.head(3))
print(df.dtypes)


# 2) 데이터 정제 (기본 예시)
# 2-1) 컬럼명 앞뒤 공백 제거
df.columns = [c.strip() for c in df.columns]

# 2-2) INSERT 컬럼 순서대로 DF 컬럼을 맞춰두기
df = df[["환자ID", "나이", "키", "몸무게", "BMI", "혈압", "간효소율"]].copy()

# 2-3) DB 컬럼명(영문)으로 바꿔서 그대로 df.values[idx]를 넣기 좋게 만듦
df.columns = ["patient_id", "age", "height_cm", "weight_kg", "bmi", "bp", "liver_enzyme_ratio"]

# 2-4) NaN -> None (DB에 NULL로 들어가게)
df = df.where(pd.notna(df), None)


# 3) DataFrame -> Python dict 변환 
records = df.to_dict(orient="records")
print(records[0]) # 첫 1행


# 4) Table 생성 
with conn.cursor() as cur:
    # # CREATE TABLE 
    # cur.execute("""
    # CREATE TABLE patient (
    #     patient_id INT PRIMARY KEY,
    #     age INT,
    #     height_cm INT,
    #     weight_kg INT,
    #     bmi DECIMAL(6,2),
    #     bp INT,
    #     liver_enzyme_ratio DECIMAL(6,2)
    # );
    # """)
    # conn.commit()

    # 5) INSERT
    sql = """INSERT INTO patient
    (patient_id, age, height_cm, weight_kg, bmi, bp, liver_enzyme_ratio)
    VALUES(%s, %s, %s, %s, %s, %s, %s);"""

    #INSERT(한 줄) - CSV 첫 번째 행 1건만 넣어보기
    first_row = tuple(df.values[0])
    cur.execute(sql, first_row)
    conn.commit()

    #INSERT(여러 줄) - CSV 전체 데이터 넣어보기
    for idx in range(1, len(df)):  # 1부터 시작 = 두 번째 행부터
        cur.execute(sql, tuple(df.values[idx]))
    conn.commit()


    # 6) DB 확인하기
    cur.execute("SELECT COUNT(*) AS cnt FROM patient;")
    print("총 행 수:", cur.fetchone())

    cur.execute("SELECT * FROM patient ORDER BY `patient_id` LIMIT 5;")
    print("데이터 5개 확인:", cur.fetchall())

conn.close()

