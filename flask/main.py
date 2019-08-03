from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS
import cv2
import io
from PIL import Image

app = Flask(__name__)
CORS(app)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/upload',methods = ['POST', 'GET'])
def upload():
    if request.method == 'GET':
        return jsonify({'GET':'SUCCESS'})
    if request.method == 'POST':
        print('Recieved POST request')

        image = request.files["file"]
        image_bytes = Image.open(io.BytesIO(image.read()))
        image_bytes.save('hello.jpg')
        return jsonify({'count':'420'})

if __name__ == '__main__':
   app.run(debug = True, port = 3000)
