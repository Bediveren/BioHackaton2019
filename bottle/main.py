from bottle import route, run, template

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

run(host='localhost', port=8080)
