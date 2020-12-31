from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/hello'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            output = ""
            output += "<html><body>"
            output += "Hello, world!"
            output += "</body></html>"

            print(output)

            self.wfile.write(output.encode('utf-8'))
        else:
            self.send_error(404)


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
