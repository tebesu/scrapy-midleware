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
