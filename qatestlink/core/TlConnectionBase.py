# -*- coding: utf-8 -*-
"""TODO: doc module"""

import requests
from qatestlink.core.xmls.XmlParserRequest import XmlParserRequest


class TlConnectionBase(object):
    """TODO: doc class"""

    url = None
    dev_key = None

    headers = {'Content-Type': 'application/xml'}
    #xml_path = 'configs/base_request.xml'

    def __init__(self, url=None, dev_key=None):
        """TODO: doc method"""
        if url is None:
            raise Exception('Can\'t connect to None url')
        self.url = url
        if dev_key is None:
            raise Exception('Can\'t connect with None dek_key')
        self.dev_key = dev_key
        # class logic
        #self.check_dev_key()

    def check_dev_key(self):
        """TODO: doc method"""
        xml_parsed = XmlParserRequest(
            dev_key=self.dev_key,
            method_name='tl.checkDevKey'
        )
        data = "<?xml version='1.0' encoding='utf-8'?>{}".format(
            xml_parsed.to_string()).replace("b'", '')
        self.request(xml_request=data)

    def request(self, method_type='POST', xml_request=None):
        """TODO: doc method"""
        if method_type != 'POST':
            raise Exception('HTTP verb not supported')
        print("making POST to url: {}".format(self.url))
        print("headers: {}".format(self.headers))
        print("data: {}".format(xml_request))
        return requests.post(url=self.url,
                             data=xml_request,
                             headers=self.headers).text
