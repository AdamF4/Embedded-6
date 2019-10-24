import cgi
import urllib
from datetime import datetime
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#import SocketServer
from http.server import BaseHTTPRequestHandler, HTTPServer
device_name="Raspberry PI"
class S(BaseHTTPRequestHandler):
 def _set_headers(self):
  self.send_response(200)
  self.send_header('Content-type', 'text/html')
  #self.send_header('Content-type', 'text/plain')
  self.end_headers()
 def do_GET(self):
  self._set_headers()
  self.wfile.write(bytes("<html><body> <h1>Hello from "+device_name+"</h1><form method=POST><label>Device name: </label><input type=text name=device_name ><input type=submit value=Submit ><input type=submit name=reboot value=Reboot></form></body></html>","utf-8"))
 def do_POST(self):
  # Read and parse POST variables as a result of FORM submit.
  #length = int(self.headers.getheader('content-length'))
  #postvars = urllib.parse_qs(self.rfile.read(length), keep_blank_values=1)
  # This is the new 'device_name'. You will need to devise some
  # way of remembering this value (hint: maybe a global variable?)
  #device_name = postvars['device_name'][0]
  # Write the HTTP response back to the web browser
  self._set_headers()
  form = cgi.FieldStorage(
      fp=self.rfile,
      headers=self.headers,
      environ={'REQUEST_METHOD': 'POST'}
  )
  global device_name
  device_name=form.getvalue("device_name")
  if 'reboot' in form.keys():
      print("Rebooting...")
      #subprocess.call("reboot", shell=True)
      self.wfile.write(bytes("<html><body>Rebooting!</body></html>","utf-8"))
  else:
   self.wfile.write(bytes("<html><body>Thanks! My new device name is <b>","utf-8"))
   self.wfile.write(bytes(device_name,"utf-8"))
   self.wfile.write(bytes("</b></body></html>","utf-8"))

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
