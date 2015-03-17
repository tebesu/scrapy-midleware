# Scrapy Middleware
Collection of some middleware. Crawl Responsibly.


## User Agent Rotator Middleware
Automatically rotates user agents for each request. Add the configurations in settings.py and modify it to your setup.



## Tor Proxy Download Handler
Configure the Tor server and port in settings.py. This is from a stack overflow [post]. Only works for HTTP requests, no support for HTTPS.


Requires txsocksx, install via pip

```
pip install txsocksx
```


[post]: https://stackoverflow.com/questions/21839676/how-to-write-a-downloadhandler-for-scrapy-that-makes-requests-through-socksipy
