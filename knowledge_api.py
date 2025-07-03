from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # 允许跨域

# 假设 knowledge.json 是上述结构
with open('knowledge.json', 'r', encoding='utf-8') as f:
    knowledge_data = json.load(f)

@app.route('/api/knowledge')
def get_knowledge():
    return jsonify(knowledge_data)

# 前端静态页面
@app.route('/')
def index():
    return send_from_directory('frontend/build', 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('frontend/build', path)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
