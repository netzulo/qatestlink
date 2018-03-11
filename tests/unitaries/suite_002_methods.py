# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""TODO: doc module"""


import logging
from unittest import TestCase
from unittest import skipIf
from qatestlink.core.utils.Utils import settings
from qatestlink.core.exceptions.response_exception import ResponseException
from qatestlink.core.testlink_manager import TLManager
from qatestlink.core.models.tl_models import TProject
from qatestlink.core.models.tl_models import TPlan
from qatestlink.core.models.tl_models import TSuite
from qatestlink.core.models.tl_models import TPlatform
from qatestlink.core.models.tl_models import TBuild
from qatestlink.core.models.tl_models import TCase


SETTINGS = settings()
API_DEV_KEY = SETTINGS['dev_key']
SKIP = SETTINGS['tests']['skip']['methods']
SKIP_MESSAGE = SETTINGS['tests']['skip_message']
DATA = SETTINGS['tests']['data']


class TestMethods(TestCase):
    """TODO: doc class"""

    @classmethod
    def setUpClass(cls):
        """TODO: doc method"""
        cls.testlink_manager = TLManager()

    def setUp(self):
        """TODO: doc method"""
        self.assertIsInstance(
            self.testlink_manager, TLManager)
        self.assertIsInstance(
            self.testlink_manager.log, logging.Logger)

    @skipIf(False, SKIP_MESSAGE)
    def test_001_method_tprojects(self):
        """TODO: doc method"""
        tprojects = self.testlink_manager.api_tprojects(
            dev_key=API_DEV_KEY)
        self.assertIsInstance(tprojects, list)
        self.assertGreater(len(tprojects), 0)
        for tproject in tprojects:
            self.testlink_manager.log.debug(repr(tproject))
            self.assertIsInstance(tproject, TProject)

    @skipIf(False, SKIP_MESSAGE)
    def test_002_method_tproject(self):
        """TODO: doc method"""
        tproject = self.testlink_manager.api_tproject(DATA['tproject_name'])
        self.assertIsInstance(tproject, TProject)
        self.assertEquals(tproject.name, DATA['tproject_name'])

    @skipIf(False, SKIP_MESSAGE)
    def test_003_method_tproject_tplans(self):
        """TODO: doc method"""
        tplans = self.testlink_manager.api_tproject_tplans(DATA['tproject_id'])
        self.assertIsInstance(tplans, list)
        self.assertGreater(len(tplans), 0)
        for tplan in tplans:
            self.testlink_manager.log.debug(repr(tplan))
            self.assertIsInstance(tplan, TPlan)

    @skipIf(False, SKIP_MESSAGE)
    def test_004_method_tproject_tsuites_first_level(self):
        """TODO: doc method"""
        tsuites = self.testlink_manager.api_tproject_tsuites_first_level(
            DATA['tproject_id'])
        self.assertIsInstance(tsuites, list)
        self.assertGreater(len(tsuites), 0)
        for tsuite in tsuites:
            self.testlink_manager.log.debug(repr(tsuite))
            self.assertIsInstance(tsuite, TSuite)

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_005_method_tplan(self):
        """TODO: doc method"""
        tplan = self.testlink_manager.api_tplan(
            DATA['tproject_name'], DATA['tplan_name'])
        self.assertIsInstance(tplan, TPlan)
        self.assertEquals(tplan.name, DATA['tplan_name'])

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_006_method_tplan_platforms(self):
        """TODO: doc method"""
        platforms = self.testlink_manager.api_tplan_platforms(
            DATA['tplan_id'])
        self.assertIsInstance(platforms, list)
        self.assertGreater(len(platforms), 0)
        for platform in platforms:
            self.testlink_manager.log.debug(repr(platform))
            self.assertIsInstance(platform, TPlatform)

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_007_method_tplan_builds(self):
        """TODO: doc method"""
        builds = self.testlink_manager.api_tplan_builds(
            DATA['tplan_id'])
        self.assertIsInstance(builds, list)
        self.assertGreater(len(builds), 0)
        for build in builds:
            self.testlink_manager.log.debug(repr(build))
            self.assertIsInstance(build, TBuild)

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_008_method_tplan_tsuites(self):
        """TODO: doc method"""
        tsuites = self.testlink_manager.api_tplan_tsuites(
            DATA['tplan_id'])
        self.assertIsInstance(tsuites, list)
        self.assertGreater(len(tsuites), 0)
        for tsuite in tsuites:
            self.testlink_manager.log.debug(repr(tsuite))
            self.assertIsInstance(tsuite, TSuite)

    @skipIf(True, SKIP_MESSAGE)
    def test_009_method_tplan_tcases(self):
        """TODO: doc method"""
        # TODO: don't skip because of yes
        tcases = self.testlink_manager.api_tplan_tcases(
            DATA['tplan_id'])
        self.assertIsInstance(tcases, list)
        self.assertGreater(len(tcases), 0)
        for tcase in tcases:
            self.testlink_manager.log.debug(repr(tcase))
            self.assertIsInstance(tcase, TCase)


class TestMethodsRaises(TestCase):
    """TODO: doc class"""

    @classmethod
    def setUpClass(cls):
        """TODO: doc method"""
        cls.testlink_manager = TLManager()

    def setUp(self):
        """TODO: doc method"""
        self.assertIsInstance(
            self.testlink_manager, TLManager)
        self.assertIsInstance(
            self.testlink_manager.log, logging.Logger)

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_001_raises_tproject_notname(self):
        """TODO: doc method"""
        self.assertRaises(
            Exception, self.testlink_manager.api_tproject)

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_002_raises_tproject_emptyname(self):
        """TODO: doc method"""
        self.assertRaises(
            ResponseException,
            self.testlink_manager.api_tproject,
            '')

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_003_raises_tproject_tplans_notid(self):
        """TODO: doc method"""
        self.assertRaises(
            Exception, self.testlink_manager.api_tproject_tplans)

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_004_raises_tproject_tplans_notfoundid(self):
        """TODO: doc method"""
        self.assertRaises(
            ResponseException,
            self.testlink_manager.api_tproject_tplans,
            -1)

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_005_raises_tproject_tsuites_first_level_notid(self):
        """TODO: doc method"""
        self.assertRaises(
            Exception, self.testlink_manager.api_tproject_tsuites_first_level)

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_006_raises_tproject_tsuites_first_level_notfoundid(self):
        """TODO: doc method"""
        self.assertRaises(
            ResponseException,
            self.testlink_manager.api_tproject_tsuites_first_level,
            -1)

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_007_raises_tplan_notname(self):
        """TODO: doc method"""
        self.assertRaises(
            Exception, self.testlink_manager.api_tplan)

    @skipIf(True, 'Test SKIPPED, waiting for issue https://github.com/viglesiasce/testlink/issues/7')
    def test_008_raises_tplan_emptytprojectname(self):
        """TODO: doc method"""
        self.assertRaises(
            ResponseException,
            self.testlink_manager.api_tplan,
            '',
            DATA['tplan_name'])

    @skipIf(True, 'Test SKIPPED, waiting for issue https://github.com/viglesiasce/testlink/issues/7')
    def test_009_raises_tplan_emptytplanname(self):
        """TODO: doc method"""
        self.assertRaises(
            ResponseException,
            self.testlink_manager.api_tplan,
            DATA['tproject_name'],
            '')

    @skipIf(True, 'Test SKIPPED, waiting for issue https://github.com/viglesiasce/testlink/issues/7')
    def test_010_raises_tplan_emptytnames(self):
        """TODO: doc method"""
        self.assertRaises(
            ResponseException,
            self.testlink_manager.api_tplan,
            '', '')

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_011_raises_tplan_platforms_notname(self):
        """TODO: doc method"""
        self.assertRaises(
            Exception, self.testlink_manager.api_tplan_platforms)

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_012_raises_tplan_platforms_notfoundid(self):
        """TODO: doc method"""
        self.assertRaises(
            ResponseException,
            self.testlink_manager.api_tplan_platforms,
            -1)

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_013_raises_tplan_builds_notid(self):
        """TODO: doc method"""
        self.assertRaises(
            Exception, self.testlink_manager.api_tplan_builds)

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_014_raises_tplan_builds_notfoundid(self):
        """TODO: doc method"""
        self.assertRaises(
            ResponseException,
            self.testlink_manager.api_tplan_builds,
            -1)

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_015_raises_tplan_tsuites_notid(self):
        """TODO: doc method"""
        self.assertRaises(
            Exception, self.testlink_manager.api_tplan_tsuites)

    @skipIf(SKIP, SKIP_MESSAGE)
    def test_016_raises_tplan_tsuites_notfoundid(self):
        """TODO: doc method"""
        self.assertRaises(
            ResponseException,
            self.testlink_manager.api_tplan_tsuites,
            -1)
