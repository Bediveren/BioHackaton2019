from bottle import route, template, run, request, post
import bottle
from bottle import response
from json import dumps

# the decorator
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


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
@enable_cors
def do_upload():
    upload = request.files.get('file')
    upload.save('.')
    print('HELLo')
    rv = [{ "id": 1, "name": "Test Item 1" }, { "id": 2, "name": "Test Item 2" }]
    response.content_type = 'application/json'
    return dumps(rv)

run(host='localhost', port=3000)
