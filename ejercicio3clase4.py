from urllib import request
from urllib.error import URLError
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.gutenberg.org/cache/epub/2000/pg2000.txt"
def count(url):
    try:
        file = request.urlopen(url, context=ctx)
    except URLError:
        return(URLError)
    else:
        content = file.read()
        return len(content.split())

print (count('https://www.gutenberg.org/cache/epub/2000/pg2000.txt'))