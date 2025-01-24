import http.server
from urllib.parse import urlparse, parse_qs
from ImportedFunctions.writeToEnv import writeToEnv

class CallBackHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        parsedURL = urlparse(self.path)
        query = parse_qs(parsedURL.query)

        from ImportedFunctions.oauth import state

        if query.get("state", "None")[0] == state:
            code = query.get("code", "None")[0]
            writeToEnv(code)
            
            print("State matches")
            self.send_response(200)
            self.end_headers()
        else:
            print("State does not match")
            self.send_response(400)
            self.send_header()

        



        