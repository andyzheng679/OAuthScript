
#https://docs.python.org/3/library/secrets.html
#https://docs.python.org/3/library/webbrowser.html
#https://docs.python.org/3/library/http.server.html
#https://docs.python.org/3/library/urllib.parse.html
from ImportedFunctions.oauth import oAuthGet
from ImportedFunctions.server import server


def main():
    oAuthGet()
    server()

    
    




if __name__ == "__main__":
    main()