# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from clay_hr_python_sdk.paths.paystub.get import GetDetails
from clay_hr_python_sdk.apis.tags.pay_stubs_api_raw import PayStubsApiRaw


class PayStubsApi(
    GetDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PayStubsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PayStubsApiRaw(api_client)
