import requesocks
from TorProxy import TorProxy
session = requesocks.session()
# Tor uses the 9050 port as the default socks port
session.proxies = TorProxy.get_proxy()
print(session.proxies)
# Make a request through the Tor connection
# IP visible through Tor
print session.get("http://httpbin.org/ip").text

# Above should print an IP different than your public IP
# Following prints your normal public IP
import requests
print requests.get("http://httpbin.org/ip").text