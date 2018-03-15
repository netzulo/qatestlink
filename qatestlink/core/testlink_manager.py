# -*- coding: utf-8 -*-
"""Testlink Managers"""


from qatestlink.core.connections.connection_base import ConnectionBase
from qatestlink.core.logger_manager import LoggerManager
from qatestlink.core.models.tl_models import TBuild
from qatestlink.core.models.tl_models import TCase
from qatestlink.core.models.tl_models import TPlan
from qatestlink.core.models.tl_models import TPlatform
from qatestlink.core.models.tl_models import TProject
from qatestlink.core.models.tl_models import TSuite
from qatestlink.core.utils import settings as settings_func
from qatestlink.core.xmls.xmlrpc_manager import XMLRPCManager


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
            list(TProject) -- list of object model for Testlink Test Project
                data
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
        """Call to method named 'tl.getTestProjectByName' for testlink XMLRPC

        Arguments:
            tproject_name {str} -- name of testlink Test Project

        Keyword Arguments:
            dev_key {str} -- string of developer key provided by Testlink
                (default: {value obtained from JSON settings file})

        Returns:
            TProject -- object model for Testlink Test Project data
        """
        if not dev_key:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tproject_by_name(
            dev_key, tproject_name)
        res = self._conn.post(self._xml_manager.headers, req_data)
        res_dict = self._xml_manager.parse_response(res)
        res_param = res_dict.get(
            'methodResponse')['params']['param']['value']
        data_properties = res_param['struct']['member']
        return TProject(data_properties)

    def api_tproject_tplans(self, tproject_id, dev_key=None):
        """Call to method named 'tl.getProjectTestPlans' for testlink XMLRPC

        Arguments:
            tproject_id {int} -- ID of Testlink Test Project to get Testlink
                Test Plan

        Keyword Arguments:
            dev_key {str} -- string of developer key provided by Testlink
                (default: {value obtained from JSON settings file})

        Returns:
            TPlan -- object model for Testlink Test Plan data
        """
        if not dev_key:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tproject_tplans(
            dev_key, tproject_id)
        res = self._conn.post(self._xml_manager.headers, req_data)
        res_dict = self._xml_manager.parse_response(res)
        res_param = res_dict.get(
            'methodResponse')['params']['param']['value']
        data_list = res_param.get('array')['data']['value']
        tplans = list()
        for data_properties in data_list:
            properties = data_properties['struct']['member']
            tplan = TPlan(properties)
            tplans.append(tplan)
        return tplans

    def api_tproject_tsuites_first_level(self, tproject_id, dev_key=None):
        """Call to method named 'tl.getFirstLevelTestSuitesForTestProject' for
            testlink XMLRPC

        Arguments:
            tproject_id {int} -- ID of Testlink Test Project to get Testlink
                Test Plan

        Keyword Arguments:
            dev_key {str} -- string of developer key provided by Testlink
                (default: {value obtained from JSON settings file})

        Returns:
            list(TSuite) -- list of object model for Testlink Test Suite
                data
        """
        if not dev_key:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tproject_tsuites_first_level(
            dev_key, tproject_id)
        res = self._conn.post(self._xml_manager.headers, req_data)
        res_dict = self._xml_manager.parse_response(res)
        res_param = res_dict.get(
            'methodResponse')['params']['param']['value']
        data_list = res_param.get('array')['data']['value']
        tsuites = list()
        for data_properties in data_list:
            properties = data_properties['struct']['member']
            tsuite = TSuite(properties)
            tsuites.append(tsuite)
        return tsuites

    def api_tplan(self, tproject_name, tplan_name, dev_key=None):
        """Call to method named 'tl.getTestPlanByName' for testlink XMLRPC

        Arguments:
            tproject_name {str} -- NAME of Testlink Test Project to get
                Testlink Test Project
            tplan_name {str} -- NAME of Testlink Test Project to get Testlink
                Test Plan

        Keyword Arguments:
            dev_key {str} -- string of developer key provided by Testlink
                (default: {value obtained from JSON settings file})

        Returns:
            TPlan -- object model for Testlink Test Plan data
        """
        if not dev_key:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tplan_by_name(
            dev_key, tproject_name, tplan_name)
        res = self._conn.post(self._xml_manager.headers, req_data)
        res_dict = self._xml_manager.parse_response(res)
        res_param = res_dict.get(
            'methodResponse')['params']['param']['value']
        data_properties = res_param.get(
            'array')['data']['value']['struct']['member']
        return TPlan(data_properties)

    def api_tplan_platforms(self, tplan_id, dev_key=None):
        """Call to method named 'tl.getTestPlanPlatforms' for testlink XMLRPC

        Arguments:
            tplan_id {int} -- ID of Testlink Test Project to get Testlink
                Test Plan

        Keyword Arguments:
            dev_key {str} -- string of developer key provided by Testlink
                (default: {value obtained from JSON settings file})

        Returns:
            list(TPlatform) -- list of object model for Testlink Platform data
        """
        if dev_key is None:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tplan_platforms(dev_key, tplan_id)
        res = self._conn.post(self._xml_manager.headers, req_data)
        res_dict = self._xml_manager.parse_response(res)
        res_param = res_dict.get(
            'methodResponse')['params']['param']['value']
        data_list = res_param.get('array')['data']['value']
        tplatforms = list()
        for data_properties in data_list:
            properties = data_properties['struct']['member']
            tplatform = TPlatform(properties)
            tplatforms.append(tplatform)
        return tplatforms

    def api_tplan_builds(self, tplan_id, dev_key=None):
        """Call to method named 'tl.getBuildsForTestPlan' for testlink XMLRPC

        Arguments:
            tplan_id {int} -- ID of Testlink Test Project to get Testlink
                Test Plan

        Keyword Arguments:
            dev_key {str} -- string of developer key provided by Testlink
                (default: {value obtained from JSON settings file})

        Returns:
            list(TBuild) -- list of object model for Testlink Build data
        """
        if not dev_key:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tplan_builds(dev_key, tplan_id)
        res = self._conn.post(self._xml_manager.headers, req_data)
        res_dict = self._xml_manager.parse_response(res)
        res_param = res_dict.get(
            'methodResponse')['params']['param']['value']
        data_list = res_param.get('array')['data']['value']
        tbuilds = list()
        for data_properties in data_list:
            properties = data_properties['struct']['member']
            tbuild = TBuild(properties)
            tbuilds.append(tbuild)
        return tbuilds

    def api_tplan_tsuites(self, tplan_id, dev_key=None):
        """Call to method named 'tl.getTestSuitesForTestPlan' for testlink
            XMLRPC

        Arguments:
            tplan_id {int} -- ID of Testlink Test Project to get Testlink
                Test Plan

        Keyword Arguments:
            dev_key {str} -- string of developer key provided by Testlink
                (default: {value obtained from JSON settings file})

        Returns:
            list(TSuite) -- list of object model for Testlink Test Suite data
        """
        if not dev_key:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tplan_tsuites(dev_key, tplan_id)
        res = self._conn.post(self._xml_manager.headers, req_data)
        res_dict = self._xml_manager.parse_response(res)
        res_param = res_dict.get(
            'methodResponse')['params']['param']['value']
        data_list = res_param.get('array')['data']['value']
        tsuites = list()
        for data_properties in data_list:
            properties = data_properties['struct']['member']
            tsuite = TSuite(properties)
            tsuites.append(tsuite)
        return tsuites

    def api_tplan_tcases(self, tplan_id, dev_key=None):
        """Call to method named 'tl.getTestCasesForTestPlan' for testlink
            XMLRPC

        Arguments:
            tplan_id {int} -- ID of Testlink Test Project to get Testlink
                Test Plan

        Keyword Arguments:
            dev_key {str} -- string of developer key provided by Testlink
                (default: {value obtained from JSON settings file})

        Returns:
            list(TCase) -- list of object model for Testlink Test Case data
        """
        if dev_key is None:
            dev_key = self._settings.get('dev_key')
        req_data = self._xml_manager.req_tplan_tcases(dev_key, tplan_id)
        res = self._conn.post(self._xml_manager.headers, req_data)
        res_dict = self._xml_manager.parse_response(res)
        res_param = res_dict.get(
            'methodResponse')['params']['param']['value']
        data_list = res_param.get('struct')['member']
        tcases = list()
        for data_properties in data_list:
            # TODO: make all assigned builds reporting to models,
            # not just first
            properties = data_properties.get(
                'value')['struct']['member'][0]['value']['struct']['member']
            tcase = TCase(properties)
            tcases.append(tcase)
        return tcases
