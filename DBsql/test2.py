import pymysql

# DB 연결
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="test1234",
    db="health_ai",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)


with conn.cursor() as cur:
    # 1. 연령대별(10살 단위) 평균 BMI + 인원수
    q1 = """
    SELECT
        FLOOR(age/10)*10 AS age_group,
        COUNT(*) AS cnt,
        ROUND(AVG(bmi), 2) AS avg_bmi
    FROM patient
    GROUP BY age_group
    ORDER BY age_group ASC;
    """
    cur.execute(q1)
    rows1 = cur.fetchall()

    print("연령대별 평균 BMI")
    for r in rows1:
        print(r)


    # 2. 고위험(혈압>=140 AND BMI>=25) 상위 10명
    q2 = """
    SELECT patient_id, age, bmi, bp, liver_enzyme_ratio
    FROM patient
    WHERE bp >= 140 AND bmi >= 25
    ORDER BY bp DESC
    LIMIT 10;
    """
    cur.execute(q2)
    rows2 = cur.fetchall()

    print("고위험 상위 10명")
    for r in rows2:
        print(r)

    # 3. 전체 평균 BMI보다 BMI가 큰 사람 수
    q3 = """
    SELECT COUNT(*) AS cnt
    FROM patient
    WHERE bmi > (
        SELECT AVG(bmi) FROM patient
    );
    """
    cur.execute(q3)
    row3 = cur.fetchone()

    print("평균 BMI보다 큰 사람 수")
    print(row3)

conn.close()
