# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import clay_hr_python_sdk
from clay_hr_python_sdk.paths.api_timesheet_activitytype_list import get
from clay_hr_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiTimesheetActivitytypeList(ApiTestMixin, unittest.TestCase):
    """
    ApiTimesheetActivitytypeList unit test stubs
        Retrieve list of activity types based on cid.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
