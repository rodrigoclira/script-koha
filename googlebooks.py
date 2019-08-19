import requests

KEY = ''

gbookurl="https://www.googleapis.com/books/v1/volumes?q=isbn:%s&key=" + KEY


def getData(urlRequest):           
    r = requests.get(url = urlRequest)
    try:   
        json = r.json()
        #descricao = r.json()["items"][0]["volumeInfo"]["description"]
        if ("error" in json):
            print (json["error"]["errors"][0]["reason"])
        else:
            webReaderLink = json["items"][0]["accessInfo"]["webReaderLink"]
            accessViewStatus = json["items"][0]["accessInfo"]["accessViewStatus"]
        if (accessViewStatus != "NONE"):
            return webReaderLink
    except KeyboardInterrupt:
        exit()
    except:
        pass
        #print (urlRequest)

fsuccs = open("succ.csv", "w")
ferrors = open("error.csv", "w")
base = open("livros.csv")
isbns = []
errors = []
succs = []

for livro in base: 
    if livro: 
        stripped = livro.strip("\n").split(",")
        current_isbn = stripped[-1]
        if current_isbn and current_isbn not in isbns:
            isbns.append(current_isbn)
            print (current_isbn)
            urlRequest = gbookurl % current_isbn
            webview = getData(urlRequest)            
            if (webview):                
                line = stripped[0] + "," + current_isbn + "," + webview + "\n"
                succs.append(line)
                print (line)
            else:
                line = stripped[0] + "," + current_isbn + "," + urlRequest + "\n"
                errors.append(line)

fsuccs.writelines(succs)
ferrors.writelines(errors)
fsuccs.close()
ferrors.close()

#print (descricao)
#print (webview)
