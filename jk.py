from flask import Flask, request, jsonify

# 初始化Flask应用
app = Flask(__name__)

# 定义POST接口，路径为/api/data
@app.route('/api/data', methods=['POST'])
def handle_data():
    try:
        # 获取请求数据（支持JSON和表单数据）
        if request.is_json:
            data = request.get_json()  # 解析JSON数据
        else:
            data = request.form.to_dict()  # 解析表单数据

        # 验证必要参数（示例：检查是否包含'name'字段）
        if not data or 'name' not in data:
            return jsonify({
                'code': 400,
                'message': '缺少必要参数：name',
                'data': None
            }), 400

        # 业务逻辑处理（这里仅做示例）
        result = {
            'received_data': data,
            'processed': f"Hello, {data['name']}!",
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        # 返回成功响应
        return jsonify({
            'code': 200,
            'message': '处理成功',
            'data': result
        }), 200

    except Exception as e:
        # 异常处理
        return jsonify({
            'code': 500,
            'message': f'服务器错误：{str(e)}',
            'data': None
        }), 500

# 启动服务（仅在直接运行脚本时执行）
if __name__ == '__main__':
    # 允许外部访问（host='0.0.0.0'），端口8000
    app.run(host='0.0.0.0', port=8000, debug=False)  # 生产环境关闭debug
