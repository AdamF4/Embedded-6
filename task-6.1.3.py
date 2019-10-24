

#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#import SocketServer
from http.server import BaseHTTPRequestHandler, HTTPServer
class S(BaseHTTPRequestHandler):
 def _set_headers(self):
  self.send_response(200)
  self.send_header('Content-type', 'text/html')
  #self.send_header('Content-type', 'text/plain')
  self.end_headers()
 def do_GET(self):
  self._set_headers()
  self.wfile.write(bytes("<html><body><h1>A Tale of Two Cities</h1><p>It was the <b>best</b> of times...</p></html>","utf-8"))

def run(server_class=HTTPServer, handler_class=S, port=8000):
 server_address = ('', port)
 httpd = server_class(server_address, handler_class)
 print('Starting httpd...')
 httpd.serve_forever()
if __name__ == "__main__":
 from sys import argv
 if len(argv) == 2:
  run(port=int(argv[1]))
 else:
  run()
