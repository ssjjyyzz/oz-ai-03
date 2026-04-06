from fastapi import FastAPI

# 127.0.0.1:8000 서버 실행치
app = FastAPI()

# Python 데코레이터: 파이썬 함수에 추가적인 기능을 부여하는 문법

# GET / 요청이 들어오면, root_handler라는 함수를 실행하라
@app.get("/")
def root_handler():
    return {"ping": "pong"}

# GET / hello 요청이 들어오면, hello_handler() 실행
@app.get("/hello")
def hello_handler():
    return {"message": "Hello from FastAPI!"}

# 임시 데이터베이스
users = [
    {"id": 1, "name": "alex", "job": "student"},
    {"id": 2, "name": "bob", "job": "sw engineer"},
    {"id": 3, "name": "chris", "job": "barista"},
]

# 전체 사용자 목록 조회 API
# GET /users
@app.get("/users")
def get_users_handler():
    return users

# 변수처리 하는 애보다 항상 고정된 애들이 위에 위치해야 함.
@app.get("/users/search")
def search_user_handler():
    return {"msg": "searching..."}
        
# 단일(특정) 사용자 데이터 조회 API
# GET /users/{user_id} -> {user_id}번 사용자 데이터 조회
@app.get("/users/{user_id}")
def get_user_handler(user_id: int):
    # if type(user_id) is not int:
    #     raise ValueError("user_id는 int만 허용됩니다.")
    for user in users:
        if user["id"] == user_id:
            return user
    
