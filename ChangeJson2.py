from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# --- 請確認此路徑正確 ---
JSON_FILE_PATH = "/Users/mariannalee/Desktop/python/musicMIDI/testgroup.json"

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/api/data')
def get_data():
    try:
        with open(JSON_FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # 使用 5001 埠號避免與系統預設衝突
    app.run(debug=True, port=5001)