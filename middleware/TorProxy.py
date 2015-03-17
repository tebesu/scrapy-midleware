# Source:
# http://stackoverflow.com/questions/21839676/how-to-write-a-downloadhandler-for-scrapy-that-makes-requests-through-socksipy
from txsocksx.http import SOCKS5Agent
from scrapy.core.downloader.handlers.http11 import HTTP11DownloadHandler, ScrapyAgent
from twisted.internet import reactor
from scrapy.xlib.tx import TCP4ClientEndpoint
from scrapy.conf import settings
# pylint: disable=C0301


class TorProxyDownloadHandler(HTTP11DownloadHandler):
    def download_request(self, request, spider):
        """Return a deferred for the HTTP download"""
        agent = ScrapyTorAgent(contextFactory=self._contextFactory,
                               pool=self._pool)
        return agent.download_request(request)


class ScrapyTorAgent(ScrapyAgent):

    def _get_agent(self, request, timeout):
        bindaddress = request.meta.get('bindaddress') or self._bindAddress
        proxy = request.meta.get('proxy')
        self.use_tor = settings['TOR']
        self.tor_server = settings['TOR_SERVER']
        self.tor_port = settings['TOR_PORT']

        proxyEndpoint = TCP4ClientEndpoint(reactor, self.tor_server,
                                           self.tor_port, timeout=timeout,
                                           bindAddress=bindaddress)
        agent = SOCKS5Agent(reactor, proxyEndpoint=proxyEndpoint)
        return agent
