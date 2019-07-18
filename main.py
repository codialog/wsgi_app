from sql import precondition
from render import not_found
from view import routes
from wsgiref.simple_server import make_server

class Application(object):

    def __init__(self, routes):
        self.routes = routes

    def __call__(self, environ, start_response):
        url = environ['PATH_INFO']
        if url not in self.routes:
            status = '404 Not Found'
            output = not_found(environ)
        else:
            status = '200 OK'
            output = routes[url](environ)
        response_headers = [('Content-type', 'text/html'),
                            ('Content-Length', str(len(output)))]
        start_response(status, response_headers)
        yield bytes(output, encoding='utf-8')


if __name__ == '__main__':
    try:
        port = 8080
        precondition.prepare_db()
        httpd = make_server('localhost', port, Application(routes))
        print('Serving on port {}...'.format(httpd.server_port))
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')


