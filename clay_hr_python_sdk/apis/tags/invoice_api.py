# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from clay_hr_python_sdk.paths.invoice.get import GetByProjectId
from clay_hr_python_sdk.apis.tags.invoice_api_raw import InvoiceApiRaw


class InvoiceApi(
    GetByProjectId,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: InvoiceApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = InvoiceApiRaw(api_client)
