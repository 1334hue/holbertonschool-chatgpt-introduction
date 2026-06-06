#!/usr/bin/python3
import http.server
import socketserver
import sys

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        except Exception as e:
            print(f"Error handling request: {e}")

if __name__ == "__main__":
    Handler = MyHandler

    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Serving HTTP on port {PORT} (http://127.0.0.1:{PORT}) ...")
            httpd.serve_forever()
    except KeyboardInterrupt:
        # Gracefully catch Ctrl+C closure requests
        print("\nServer stopped cleanly.")
        sys.exit(0)
    except Exception as e:
        print(f"Server error occurred: {e}")
        sys.exit(1)
