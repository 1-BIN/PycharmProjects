# pip install flask
# pip install flask-cors
from flask import Flask, render_template, request
import requests
import json
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, 1Bin!"

@app.route("/hello")
def hello():
    # jinja2 템플릿 언어로 데이터 매핑
    return render_template("hello.html", content="전달 내용", name="1BIN")

@app.route("/coin", methods=['GET', 'POST'])
def coin():
    if request.method == 'POST':
        print("post 요청 왔어요")
        data = json.loads(request.get_data())
        print(data)
        res = requests.get("https://api.upbit.com/v1/ticker?markets=" + data['market'])
        return res.content

    elif request.method == 'GET':
        res = requests.get("https://api.upbit.com/v1/market/all")
        coin_list = json.loads(res.content)
        return render_template("coin.html", coins=coin_list)


if __name__ == '__main__':
    # app.run(debug=True) #로컬호스트로 접속
     app.run(debug=True, port=5500, host="0.0.0.0") #사용자ip로 접속?