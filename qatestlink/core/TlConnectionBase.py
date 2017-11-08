# -*- coding: utf-8 -*-
# pylint: disable=no-self-use
"""TODO: doc module"""


import requests
from qatestlink.core.xmls.XmlRequest import XmlRequest
from qatestlink.core.xmls.XmlResponse import XmlResponse
from qatestlink.core.TlRequest import TlRequest as REQUEST


class TlConnectionBase(object):
    """TODO: doc class"""

    url = None
    dev_key = None
    headers = None

    def __init__(self, url, dev_key):
        """
        Args:
            url: xmlrpc testlink url
            dev_key: xmlrpc API devKey
        """
        if url is None:
            raise Exception('Can\'t connect to None url')
        self.url = url
        if dev_key is None:
            raise Exception('Can\'t connect with None dek_key')
        self.dev_key = dev_key
        self.headers = {'Content-Type': 'application/xml'}

    def post(self, req):
        """Do POST request and return response"""
        # DEBUG purpose, print
        print("POST to url: {}".format(self.url))
        print("headers: {}".format(self.headers))
        if req is None and isinstance(req, XmlRequest):
            raise Exception('Can\'t return None response')
        # DEBUG purpose, print
        print("data:\n{}".format(req.prettify()))
        res = requests.post(
            url=self.url,
            data=req.prettify(),
            headers=self.headers)
        # DEBUG purpose, print
        print("RESPONSE from url: {}".format(self.url))
        print("body:\n{}".format(res.text))
        return res

    def parse_request(self, method_name):
        """
        Need req instance of XmlRequest
        Return requests library POST.text string
        """
        xml_req = XmlRequest(dev_key=self.dev_key, method_name=method_name)
        # DEBUG purpose, print
        print("Xml request parsed:\n{}".format(xml_req.xml_str))
        return xml_req

    def parse_response(self, method_name, res_str):
        """TODO: doc method"""
        if res_str is None:
            raise Exception('Can\'t return None response')
        xml_res = XmlResponse(
            xml_str=res_str,
            method_name=method_name)
        # DEBUG purpose, print
        print("Xml response parsed:\n{}".format(xml_res.xml_str))
        return xml_res

    def check_dev_key(self):
        """Return XmlResponse parsed for method_name"""
        method_name = REQUEST.TLINK_CHECK_DEV_KEY.value
        xml_req = self.parse_request(method_name)
        post_res = self.post(xml_req)
        xml_res = self.parse_response(method_name, post_res.text)
        return xml_res

    def test_projects(self):
        """TODO: doc method"""
        method_name = REQUEST.TPROJECTS.value
        # DEBUG purpose, print
        print("method_name: {}".format(method_name))
        xml_req = self.parse_request(method_name)
        post_res = self.post(xml_req)
        xml_res = self.parse_response(method_name, post_res.text)
        return xml_res
