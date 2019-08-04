from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS
import cv2
import io
from recog import count_cells
from flask import send_file

app = Flask(__name__)
CORS(app)

@app.route('/get_image')
def get_image():
    return send_file("result.jpeg", mimetype='image/gif')

@app.route('/upload',methods = ['POST', 'GET'])
def upload():
    if request.method == 'GET':
        return jsonify({'GET':'SUCCESS'})
    if request.method == 'POST':
        imagefile = request.files.get('file', '')
        print('Recieved POST request')
        from PIL import Image
        image = request.files["file"]
        image_bytes = Image.open(io.BytesIO(image.read()))
        image_bytes.save('ImageRecieved.jpg')
        cell_count = count_cells()
        print(cell_count)
        return jsonify({'count': str(cell_count)})

if __name__ == '__main__':
   app.run(debug = True, port = 3000)
