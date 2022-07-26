from http.server import HTTPServer, BaseHTTPRequestHandler
class Index (BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response( 200 )
		self.send_header( "Content-Type" , "text/html" )
		self.end_headers()
		self.wfile.write("<h1>Restaurante da Natal</h1><button>Login</button>" .encode( "utf-8" ))
app = HTTPServer(( "0.0.0.0" , 8000 ), Index)
app.serve_forever()
