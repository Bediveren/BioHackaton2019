from bottle import route, run, template

@route('/')
def index():
    return '<b>Hello</b>!'

@route('/hello/<name>')
def example(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
