# -*- coding: utf-8 -*-
"""Testlink Managers"""


import json
import logging
import requests
from qatestlink.core.connections.connection_base import ConnectionBase
from qatestlink.core.utils.Utils import read_file
from qatestlink.core.xmls.route_type import RouteType
from qatestlink.core.xmls.request_handler import RequestHandler


PATH_CONFIG = 'qatestlink/configs/settings.json'

class TestlinkManager(object):
    """
    This class allows to send, handle and interpretate reponses
     to/from testlink api XMLRPC
    """

    _settings_path = None
    _settings = None
    _logger_manager = None
    _xml_manager = None
    _conn = None

    log = None

    def __init__(self, settings_path=None, settings=None):
        """
        This instance allow to handle requests+reponses to/from XMLRPC
        just need settings_path and settings dict loaded to works

        :Args:
            settings_path: Path for search JSON
                file with settings values
            settings: Load settings at default path,
                'qatestlink/configs/settings.json'
        """
        if settings is None:
            settings = self.get_settings(json_path=settings_path)
        self._settings = settings
        self._logger_manager = LoggerManager()
        self.log = self._logger_manager.log
        self._xml_manager = XMLRPCManager(self.log)
        # generate url using settings
        conn = self._settings.get('connection')
        self._conn = ConnectionBase(
            self.log,
            host=conn.get('host'),
            port=conn.get('port'),
            is_https=conn.get('is_https'))

    def get_settings(self, json_path=None):
        """
        Get default settings path or search on param path
         to load as a dict and return it
        """
        json_path_selected = PATH_CONFIG
        if json_path is not None:
            json_path_selected = json_path
        return read_file(file_path=json_path_selected, is_json=True)

    def api_login(self, dev_key=None):
        """Call to method named 'checkDevKey' for testlink XMLRPC"""
        if dev_key is None:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.check_dev_key(dev_key)
        res_data = self._conn.post(self._xml_manager.headers, req_data)
        #TODO: response_handler time
        #self.xml
        raise NotImplementedError('TODO: do request, and handle response')


class XMLRPCManager(object):
    """
    Manage all XMLRPCManager requests,
     responses and handle errors. This class
     store all official methods names used
     on original XMLRPC php class
    """
    _request_handler = None
    _reponse_handler = None
    _error_handler = None

    log = None
    headers = None

    def __init__(self, log):
        self.log = log
        self._request_handler = RequestHandler(self.log)
        self._reponse_handler = None
        self._error_handler = None
        self.headers = {'Content-Type': 'application/xml'}

    def check_dev_key(self, dev_key):
        """
        :return:
            And string xml object ready to use on API call
        """
        req = self._request_handler.create(
            RouteType.TLINK_CHECK_DEV_KEY)
        return self._request_handler.add_param(
            req, 'struct', 'devKey', dev_key)



class LoggerManager(object):
    """Start logger named 'qatestlink' with DEBUG level and just with console reporting"""

    log = None

    def __init__(self):
        """Start logger"""
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_level = logging.DEBUG
        logger = logging.getLogger('qatestlink')
        logger_stream = logging.StreamHandler()
        logger.setLevel(log_level)
        logger_stream.setLevel(log_level)
        logger_stream.setFormatter(formatter)
        logger.addHandler(logger_stream)
        # alias to improve logging calls
        self.log = logger
        