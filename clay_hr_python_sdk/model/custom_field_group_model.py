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


class CustomFieldGroupModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            access = schemas.StrSchema
            cfgroupid = schemas.Int32Schema
            cfgroupname = schemas.StrSchema
            cid = schemas.Int32Schema
        
            @staticmethod
            def createts() -> typing.Type['Timestamp']:
                return Timestamp
            hasCustomFields = schemas.BoolSchema
            layout = schemas.StrSchema
            objectType = schemas.StrSchema
            sequence = schemas.Int32Schema
            usergroupid = schemas.Int32Schema
            __annotations__ = {
                "access": access,
                "cfgroupid": cfgroupid,
                "cfgroupname": cfgroupname,
                "cid": cid,
                "createts": createts,
                "hasCustomFields": hasCustomFields,
                "layout": layout,
                "objectType": objectType,
                "sequence": sequence,
                "usergroupid": usergroupid,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access"]) -> MetaOapg.properties.access: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cfgroupid"]) -> MetaOapg.properties.cfgroupid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cfgroupname"]) -> MetaOapg.properties.cfgroupname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createts"]) -> 'Timestamp': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasCustomFields"]) -> MetaOapg.properties.hasCustomFields: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["layout"]) -> MetaOapg.properties.layout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["objectType"]) -> MetaOapg.properties.objectType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequence"]) -> MetaOapg.properties.sequence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usergroupid"]) -> MetaOapg.properties.usergroupid: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["access", "cfgroupid", "cfgroupname", "cid", "createts", "hasCustomFields", "layout", "objectType", "sequence", "usergroupid", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access"]) -> typing.Union[MetaOapg.properties.access, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cfgroupid"]) -> typing.Union[MetaOapg.properties.cfgroupid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cfgroupname"]) -> typing.Union[MetaOapg.properties.cfgroupname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createts"]) -> typing.Union['Timestamp', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasCustomFields"]) -> typing.Union[MetaOapg.properties.hasCustomFields, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["layout"]) -> typing.Union[MetaOapg.properties.layout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["objectType"]) -> typing.Union[MetaOapg.properties.objectType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sequence"]) -> typing.Union[MetaOapg.properties.sequence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usergroupid"]) -> typing.Union[MetaOapg.properties.usergroupid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["access", "cfgroupid", "cfgroupname", "cid", "createts", "hasCustomFields", "layout", "objectType", "sequence", "usergroupid", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        access: typing.Union[MetaOapg.properties.access, str, schemas.Unset] = schemas.unset,
        cfgroupid: typing.Union[MetaOapg.properties.cfgroupid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cfgroupname: typing.Union[MetaOapg.properties.cfgroupname, str, schemas.Unset] = schemas.unset,
        cid: typing.Union[MetaOapg.properties.cid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        createts: typing.Union['Timestamp', schemas.Unset] = schemas.unset,
        hasCustomFields: typing.Union[MetaOapg.properties.hasCustomFields, bool, schemas.Unset] = schemas.unset,
        layout: typing.Union[MetaOapg.properties.layout, str, schemas.Unset] = schemas.unset,
        objectType: typing.Union[MetaOapg.properties.objectType, str, schemas.Unset] = schemas.unset,
        sequence: typing.Union[MetaOapg.properties.sequence, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        usergroupid: typing.Union[MetaOapg.properties.usergroupid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFieldGroupModel':
        return super().__new__(
            cls,
            *args,
            access=access,
            cfgroupid=cfgroupid,
            cfgroupname=cfgroupname,
            cid=cid,
            createts=createts,
            hasCustomFields=hasCustomFields,
            layout=layout,
            objectType=objectType,
            sequence=sequence,
            usergroupid=usergroupid,
            _configuration=_configuration,
            **kwargs,
        )

from clay_hr_python_sdk.model.timestamp import Timestamp
