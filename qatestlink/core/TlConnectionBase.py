"""TODO: doc module"""


import requests
from qatestlink.core.utils.Utils import read_file


class TlConnectionBase(object):
    """TODO: doc class"""

    xml_login = read_file(file_path='configs/api_login.xml')
    xml_get_projects = read_file(file_path='configs/api_get_projects.xml')
    headers = {'Content-Type': 'application/xml'}

    def __init__(self):
        """TODO: doc method"""

        print(requests.post(
            'http://qalab.tk:86/lib/api/xmlrpc/v1/xmlrpc.php',
            data=self.xml_login.encode(encoding='utf_8'),
            headers=self.headers).text)

        print(requests.post(
            'http://qalab.tk:86/lib/api/xmlrpc/v1/xmlrpc.php',
            data=self.xml_get_projects.encode(encoding='utf_8'),
            headers=self.headers).text)


if __name__ == "__main__":
    testlink = TlConnectionBase()