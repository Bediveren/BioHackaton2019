from bottle import route, run, template
import bottle

@route('/')
def index():
    from bottle import response
    from json import dumps
    rv = [{ "id": 1, "name": "Test Item 1" }, { "id": 2, "name": "Test Item 2" }]
    response.content_type = 'application/json'
    return dumps(rv)

@route('/hello/<name>')
def example(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/upload', method='POST')
def do_upload():
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        return "File extension not allowed."

    return "File successfully recieved... probably.".

run(host='localhost', port=8080)
