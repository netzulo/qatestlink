# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""Testlink Managers"""


import xmltodict
from qatestlink.core.utils.Utils import settings as settings_func
from qatestlink.core.utils.logger_manager import LoggerManager
from qatestlink.core.connections.connection_base import ConnectionBase
from qatestlink.core.xmls.xmlrpc_manager import XMLRPCManager
from qatestlink.core.models.tl_models import TProject


PATH_CONFIG = 'qatestlink/configs/settings.json'


class TLManager(object):
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

    def __init__(self, file_path=None, file_name=None, settings=None):
        """
        This instance allow to handle requests+reponses to/from XMLRPC
        just need settings_path and settings dict loaded to works

        :Args:
            settings_path: Path for search JSON
                file with settings values
            settings: Load settings at default path,
                'qatestlink/configs/settings.json'
        """
        if not settings:
            if not file_path or not file_name:
                settings = settings_func()
            else:
                settings = settings_func(
                    file_path=file_path,
                    file_name=file_name)
        self._settings = settings
        self._logger_manager = LoggerManager(
            self._settings.get('log_level'))
        self.log = self._logger_manager.log
        self._xml_manager = XMLRPCManager(self.log)
        # generate url using settings
        conn = self._settings.get('connection')
        self._conn = ConnectionBase(
            self.log,
            host=conn.get('host'),
            port=conn.get('port'),
            is_https=conn.get('is_https'))

    def api_login(self, dev_key=None):
        """Call to method named 'checkDevKey' for testlink XMLRPC

        Keyword Arguments:
            dev_key {str} -- string of developer key provided by Testlink
                (default: {value obtained from JSON settings file})

        Returns:
            bool -- check if developer key it's valid for Testlink
        """
        if not dev_key:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_check_dev_key(dev_key)
        res = self._conn.post(self._xml_manager.headers, req_data)
        res_dict = self._xml_manager.parse_response(res)
        res_value = res_dict.get(
            'methodResponse')['params']['param']['value']
        if res_value.get('boolean'):
            return bool(res_value.get('boolean'))
        self._xml_manager.parse_errors(res_dict)

    def api_tprojects(self, dev_key=None):
        """Call to method named 'tl.getProjects' for testlink XMLRPC

        Keyword Arguments:
            dev_key {str} -- string of developer key provided by Testlink
                (default: {value obtained from JSON settings file})

        Returns:
            list(TProject) -- TODO
        """

        if not dev_key:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tprojects(dev_key)
        res = self._conn.post(self._xml_manager.headers, req_data)
        res_dict = self._xml_manager.parse_response(res)
        res_param = res_dict.get(
            'methodResponse')['params']['param']['value']
        data_list = res_param.get('array')['data']['value']
        tprojects = list()
        for data_properties in data_list:
            properties = data_properties['struct']['member']
            tproject = TProject(properties)
            tprojects.append(tproject)
        return tprojects

    def api_tproject(self, tproject_name, dev_key=None):
        """Call to method named 'tl.getTestProjectByName'"""
        if dev_key is None:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tproject_by_name(
            dev_key, tproject_name)
        res = self._conn.post(self._xml_manager.headers, req_data)
        self._xml_manager.parse_errors(res.text)
        res_as_model = self._xml_manager.res_tproject_by_name(
            res.status_code, res.text, as_model=True)
        return res_as_model

    def api_tproject_tplans(self, tproject_id, dev_key=None):
        """Call to method named 'tl.getProjectTestPlans'"""
        if dev_key is None:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tproject_tplans(
            dev_key, tproject_id)
        res = self._conn.post(self._xml_manager.headers, req_data)
        self._xml_manager.parse_errors(res.text)
        res_as_models = self._xml_manager.res_tproject_tplans(
            res.status_code, res.text, as_models=True)
        return res_as_models

    def api_tproject_tsuites_first_level(self, tproject_id, dev_key=None):
        """Call to method named 'tl.getFirstLevelTestSuitesForTestProject'"""
        if dev_key is None:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tproject_tsuites_first_level(
            dev_key, tproject_id)
        res = self._conn.post(self._xml_manager.headers, req_data)
        self._xml_manager.parse_errors(res.text)
        res_as_models = self._xml_manager.res_tproject_tsuites_first_level(
            res.status_code, res.text, as_models=True)
        return res_as_models

    def api_tplan(self, tproject_name, tplan_name, dev_key=None):
        """Call to method named 'tl.getTestPlanByName'"""
        if dev_key is None:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tplan_by_name(
            dev_key, tproject_name, tplan_name)
        res = self._conn.post(self._xml_manager.headers, req_data)
        self._xml_manager.parse_errors(res.text)
        res_as_model = self._xml_manager.res_tplan_by_name(
            res.status_code, res.text, as_model=True)
        return res_as_model

    def api_tplan_platforms(self, tplan_id, dev_key=None):
        """Call to method named 'tl.getTestPlanPlatforms'"""
        if dev_key is None:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tplan_platforms(
            dev_key, tplan_id)
        res = self._conn.post(self._xml_manager.headers, req_data)
        self._xml_manager.parse_errors(res.text)
        res_as_models = self._xml_manager.res_tplan_platforms(
            res.status_code, res.text, as_models=True)
        return res_as_models

    def api_tplan_builds(self, tplan_id, dev_key=None):
        """Call to method named 'tl.getBuildsForTestPlan'"""
        if dev_key is None:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tplan_builds(
            dev_key, tplan_id)
        res = self._conn.post(self._xml_manager.headers, req_data)
        self._xml_manager.parse_errors(res.text)
        res_as_models = self._xml_manager.res_tplan_builds(
            res.status_code, res.text, as_models=True)
        return res_as_models

    def api_tplan_tsuites(self, tplan_id, dev_key=None):
        """Call to method named 'tl.getTestSuitesForTestPlan'"""
        if dev_key is None:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tplan_tsuites(
            dev_key, tplan_id)
        res = self._conn.post(self._xml_manager.headers, req_data)
        self._xml_manager.parse_errors(res.text)
        res_as_models = self._xml_manager.res_tplan_tsuites(
            res.status_code, res.text, as_models=True)
        return res_as_models

    def api_tplan_tcases(self, tplan_id, dev_key=None):
        """Call to method named 'tl.getTestCasesForTestPlan'"""
        if dev_key is None:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tplan_tcases(
            dev_key, tplan_id)
        res = self._conn.post(self._xml_manager.headers, req_data)
        self._xml_manager.parse_errors(res.text)
        res_as_models = self._xml_manager.res_tplan_tcases(
            res.status_code, res.text, as_models=True)
        return res_as_models
