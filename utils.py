
import urllib
import urllib2
import lxml.etree as etree


def read_url(url, data=None, headers={}):
    """Read given url with given data and headers"""
    if data is not None:
      request = urllib2.Request(url, data=urllib.urlencode(data),
                                headers=headers)
    else:
      request = urllib2.Request(url, headers=headers)

    response = urllib2.urlopen(request)
    return response


def parse(url, data=None, headers={}):
    """Parse xml for given url"""
    return etree.parse(read_url(url, data, headers)).getroot()
