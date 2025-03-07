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


class GoalsGetGoalResponseAssignedUserModelLocationModelAddressModelListItemCountryModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            countryId = schemas.StrSchema
            countryName = schemas.StrSchema
            iso2 = schemas.StrSchema
            __annotations__ = {
                "countryId": countryId,
                "countryName": countryName,
                "iso2": iso2,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryId"]) -> MetaOapg.properties.countryId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryName"]) -> MetaOapg.properties.countryName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso2"]) -> MetaOapg.properties.iso2: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["countryId", "countryName", "iso2", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryId"]) -> typing.Union[MetaOapg.properties.countryId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryName"]) -> typing.Union[MetaOapg.properties.countryName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso2"]) -> typing.Union[MetaOapg.properties.iso2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["countryId", "countryName", "iso2", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        countryId: typing.Union[MetaOapg.properties.countryId, str, schemas.Unset] = schemas.unset,
        countryName: typing.Union[MetaOapg.properties.countryName, str, schemas.Unset] = schemas.unset,
        iso2: typing.Union[MetaOapg.properties.iso2, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GoalsGetGoalResponseAssignedUserModelLocationModelAddressModelListItemCountryModel':
        return super().__new__(
            cls,
            *args,
            countryId=countryId,
            countryName=countryName,
            iso2=iso2,
            _configuration=_configuration,
            **kwargs,
        )
