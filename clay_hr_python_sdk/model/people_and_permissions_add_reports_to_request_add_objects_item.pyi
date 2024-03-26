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


class PeopleAndPermissionsAddReportsToRequestAddObjectsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            adpAssociateOID = schemas.StrSchema
            managerId = schemas.Int32Schema
            relationType = schemas.StrSchema
            startDate = schemas.DateSchema
            endDate = schemas.DateSchema
            __annotations__ = {
                "adpAssociateOID": adpAssociateOID,
                "managerId": managerId,
                "relationType": relationType,
                "startDate": startDate,
                "endDate": endDate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adpAssociateOID"]) -> MetaOapg.properties.adpAssociateOID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["managerId"]) -> MetaOapg.properties.managerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationType"]) -> MetaOapg.properties.relationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["adpAssociateOID", "managerId", "relationType", "startDate", "endDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adpAssociateOID"]) -> typing.Union[MetaOapg.properties.adpAssociateOID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["managerId"]) -> typing.Union[MetaOapg.properties.managerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationType"]) -> typing.Union[MetaOapg.properties.relationType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["adpAssociateOID", "managerId", "relationType", "startDate", "endDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        adpAssociateOID: typing.Union[MetaOapg.properties.adpAssociateOID, str, schemas.Unset] = schemas.unset,
        managerId: typing.Union[MetaOapg.properties.managerId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        relationType: typing.Union[MetaOapg.properties.relationType, str, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, date, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, date, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PeopleAndPermissionsAddReportsToRequestAddObjectsItem':
        return super().__new__(
            cls,
            *args,
            adpAssociateOID=adpAssociateOID,
            managerId=managerId,
            relationType=relationType,
            startDate=startDate,
            endDate=endDate,
            _configuration=_configuration,
            **kwargs,
        )
