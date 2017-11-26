# -*- coding: utf-8 -*-
"""Testlink Managers"""


import json
import logging
from qatestlink.core.connections.connection_base import ConnectionBase
from qatestlink.core.utils.Utils import read_file
from qatestlink.core.xmls.route_type import RouteType


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
        self._xml_manager = XMLRPCManager()

    def get_settings(self, json_path=None):
        """
        Get default settings path or search on param path
         to load as a dict and return it
        """
        json_path_selected = PATH_CONFIG
        if json_path is not None:
            json_path_selected = json_path
        return read_file(file_path=json_path_selected, is_json=True)

    def api_login(self):
        """Call to method named 'checkDevKey' for testlink XMLRPC"""
        # TODO: response must be dict({}) wit data returned
        response = self._xml_manager.check_dev_key(self._settings['dev_key'])
        self.log.warning('Not Implemented')


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

    def __init__(self):
        self._request_handler = None
        self._reponse_handler = None
        self._error_handler = None

    def check_dev_key(self, dev_key):
        """
        :return:
            And string xml object ready to use on API call
        """
        request = self._request_handler.create(
            method_name=RouteType.TLINK_CHECK_DEV_KEY)
        self._request_handler.add_param(
            request,
            "struct", # param type
            "devKey", # param name
            dev_key) # param value
        return request




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
        