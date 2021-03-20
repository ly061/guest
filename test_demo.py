import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import json

app = FastAPI()  # 必须实例化该类，启动的时候调用

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8080/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 请求验证码
@app.get('/captcha')
def index():
    s = random.randint(1, 99)
    return {"data": {
        'message': f'获取验证码成功！--{s}', 'code': 200
    }}


# post登录
@app.post('/login')
def login():
    return {'message': '登录成功',
            'code': 200,
            "obj": {
                "tokenHead": "Bearer",
                "token": "adasda3wqwdqwdqwdqwd12q3wd1q21wd2q3wd1q2w1d"
            }
            }


# 请求菜单
@app.get('/system/config/menu')
def get_menu():
    with open('data.json', encoding='utf8') as f:
        data = f.read()
    data = json.loads(data)
    return data


if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=8088)
    print(get_menu())