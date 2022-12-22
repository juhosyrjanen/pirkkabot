from http.server import BaseHTTPRequestHandler
from check_price import * 

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        price = define_price()
        self.wfile.write(price)
        return
