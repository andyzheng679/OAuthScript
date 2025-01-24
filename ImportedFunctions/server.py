from http.server import HTTPServer
from ImportedFunctions.callBackHandler import CallBackHandler
def server():
    addressPort = ("localhost", 8080)

    https = HTTPServer(addressPort, CallBackHandler)
    https.timeout = 10
    print("Waiting for callback, 10 second timer")

    try:
        https.handle_request()
    except Exception as e:
        print(f"Error: {e}")
    
    print("Done")