def wsgi_application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    return ["\r\n".join(environ['QUERY_STRING'].split("&"))]
