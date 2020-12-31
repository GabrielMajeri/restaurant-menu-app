from database import DBSession, Restaurant

from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi


class RequestHandler(BaseHTTPRequestHandler):
    def begin_page(self, title: str) -> None:
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        header = "<html lang='en'>"
        header += f"<head><title>{title}</title></head>"
        header += "<body><main>"

        self.wfile.write(header.encode())

    def end_page(self):
        footer = "</main></body>"
        footer += "</html>"

        self.wfile.write(footer.encode())

    def not_found(self) -> None:
        self.send_error(404)

    def do_GET(self):
        if self.path == '/restaurants':
            self.begin_page('Restaurants list')

            body = ""

            body += "<div>"
            body += "<a href='/restaurants/create'>Add new restaurant</a>"
            body += "</div>"

            session = DBSession()

            restaurants = session.query(Restaurant).all()
            for r in restaurants:
                body += "<div>"
                body += f"<h3>{r.name}</h3>"
                body += f"<a href='/restaurants/{r.id}/edit'>Edit</a>"
                body += "&nbsp;"
                body += f"<a href='/restaurants/{r.id}/delete'>Delete</a>"
                body += "</div>"

            session.commit()

            self.wfile.write(body.encode())

            self.end_page()
        else:
            self.not_found()

    def do_POST(self):
        self.not_found()


def main():
    # Base.metadata.create_all(engine)

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
