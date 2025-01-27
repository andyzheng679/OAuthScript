importing http.server since it provides the BaseHTTPRequestHandler.
importing urlparse, parse_qs from urllib.parse to parse the url, urlparse is used to parse the url into components like scheme, netloc, path, query. parse_qs is used in this case to pase the query string into a dictionary. 
importing writeToEnv to write to the env file, specifically the authorization code from the oauth.

class CallBackHandler(http.server.BaseHTTPRequestHandler): CallBackhandler is a subclass that inherits from the BaseHTTPRequestHandler class provided by http.server. By inheriting this class, we can create custom request handling, do_GET, do_POST.

def do_GET(self): custom method, self means instance of the class, when a HTTP GET request is received by the server, an instance of the CallBackHandler class is created to handle that request, the self represents that instance. self.path is the URL path. parsedURL breaks down the self.path into components, query takes the query string from parsedURL and convertis it into a dictionary(map). Then we import the global variable state. if the query's state is equal to the state that was imported, then  get the code that is in the query and call the writeToEnv to write the code in the env file. self.send_response(200) means that it will send a status code (200), self.end_headers() 
