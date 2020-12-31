from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            output = ""
            output += "<html><body>"
            output += "<form method='POST' enctype='multipart/form-data' action='/'>"
            output += "<h2>What would you like me to say?</h2>"
            output += "<input name='message' type='text'/>"
            output += "<input type='submit' value='Submit'/>"
            output += "</form>"
            output += "</body></html>"

            print(output)

            self.wfile.write(output.encode())
        elif self.path.endswith('/hello'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            output = ""
            output += "<html><body>"
            output += "Hello, world!"
            output += "</body></html>"

            print(output)

            self.wfile.write(output.encode())
        elif self.path.endswith('/hola'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            output = ""
            output += "<html><body>"
            output += "¡Hola Mundo!"
            output += "<br/>"
            output += "<a href='/hello'>English version</a>"
            output += "</body></html>"

            print(output)

            self.wfile.write(output.encode())
        else:
            self.send_error(404)

    def do_POST(self):
        self.send_response(200)
        self.end_headers()

        message = ""
        ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))
        if ctype == 'multipart/form-data':
            pdict['boundary'] = pdict['boundary'].encode()
            fields = cgi.parse_multipart(self.rfile, pdict)
            message = fields.get('message')[0]

        output = ""
        output += "<html><body>"
        output += "<h2>Custom greeting</h2>"
        output += f"<strong>{message}</strong>"
        output += "<br/>"
        output += "<a href='/'>Go back</a>"
        output += "</body></html>"

        print(output)

        self.wfile.write(output.encode())


def main():
    port = 8080
    server_address = ('', port)
    server = HTTPServer(server_address, RequestHandler)

    print(f"Starting server on http://localhost:{port}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Keyboard interrupt received, stopping web server")
        server.shutdown()


if __name__ == '__main__':
    main()
