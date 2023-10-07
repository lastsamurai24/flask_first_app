from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello,World"


@app.route("/GoodBye")
def GoodBye():
    return "Goodday"


 # あいさつする関数を作成
@app.route("/about/<name>")
def hi(name):
    return f" {name}'s profile"

# HTMLを直接代入
@app.route("/hello")
def hello():
    html = "<html><body><h1>Hello</h1></body></html>"
    return html

# HTMLに変更
@app.route("/profile/<name>")
def profile(name):
    html = f"<html><body><h1>Hello {name}</h1></body></html>"
    return html
  
if __name__ == "__main__":
    # 使用するポートを明示
    app.run(port=8080, debug=True)
