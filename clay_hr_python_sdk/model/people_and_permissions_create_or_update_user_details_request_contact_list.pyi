# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from clay_hr_python_sdk import schemas  # noqa: F401


class PeopleAndPermissionsCreateOrUpdateUserDetailsRequestContactList(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Contact detail of user
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['PeopleAndPermissionsCreateOrUpdateUserDetailsRequestContactListItem']:
            return PeopleAndPermissionsCreateOrUpdateUserDetailsRequestContactListItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['PeopleAndPermissionsCreateOrUpdateUserDetailsRequestContactListItem'], typing.List['PeopleAndPermissionsCreateOrUpdateUserDetailsRequestContactListItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PeopleAndPermissionsCreateOrUpdateUserDetailsRequestContactList':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'PeopleAndPermissionsCreateOrUpdateUserDetailsRequestContactListItem':
        return super().__getitem__(i)

from clay_hr_python_sdk.model.people_and_permissions_create_or_update_user_details_request_contact_list_item import PeopleAndPermissionsCreateOrUpdateUserDetailsRequestContactListItem
