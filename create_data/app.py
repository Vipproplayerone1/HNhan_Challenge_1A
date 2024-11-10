from flask import Flask, render_template, request, jsonify
from PIL import Image
import io
import base64
import os
import time

app = Flask(__name__)

# Đảm bảo các thư mục lưu trữ tồn tại
os.makedirs('data/0', exist_ok=True)
os.makedirs('data/3', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_image', methods=['POST'])
def save_image():
    data = request.json
    img_data = data['image']
    digit = data['digit']  # '0' hoặc '3'

    # Decode base64 thành ảnh
    img_data = base64.b64decode(img_data.split(',')[1])
    img = Image.open(io.BytesIO(img_data))
    img = img.convert("L")  # Chuyển ảnh sang đen trắng

    # Lưu ảnh
    img_path = f"data/{digit}/{int(time.time())}.png"
    img.save(img_path)

    return jsonify({"message": "Image saved successfully."})

if __name__ == '__main__':
    app.run(debug=True)
