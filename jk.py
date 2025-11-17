# app.py
from flask import Flask, jsonify

app = Flask(__name__)

# 定义一个GET接口，路径为/api/hello
@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"status": "success", "message": "万富豪你看看可以不!"})

if __name__ == "__main__":
    # 关键：host=0.0.0.0允许外部访问，port指定端口（如5000）

    app.run(host="0.0.0.0", port=5000, debug=False)  # 生产环境关闭debug
