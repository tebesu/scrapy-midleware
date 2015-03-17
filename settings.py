'''
Filename for useragents. File should be in the same directory as the middleware
'''
USER_AGENT_LIST = 'useragents.txt'

DOWNLOADER_MIDDLEWARES = {
    # Disable Default User Agent Middleware
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,

    # Enable our user agent switcher
    # You may need to change this depending on your directory setup
    'middleware.UserAgents.UserAgentsMiddleware': 100
}





'''
Uses Tor, comment out if you dont want to use it
'''
# Tor Server configurations
TOR_SERVER = '127.0.0.1'
TOR_PORT = 9050

DOWNLOAD_HANDLERS = {
    # we dont have a handler for https
    'https': None,

    ## Enable our tor download handler
    'http': 'middleware.TorProxy.TorProxyDownloadHandler'
}
